import requests

from tonpy import LiteClient, Cell, get_block_info, BlockId, BlockIdExt, \
    Address, Emulator, begin_cell, StackEntry, VmDict, CellSlice

from tonpy.utils.shard_account import shard_is_ancestor, shard_child
from tonpy.libs.python_ton import Bits256, globalSetVerbosity
from tonpy.autogen.block import Account, Transaction, Block, BlockInfo, BlockExtra, MessageAny, AccountState
from tqdm import tqdm
from tonpy.utils.chunks import chunks
from multiprocess.pool import ThreadPool
from multiprocess import Pool
from time import sleep

#
# globalSetVerbosity(-1)

serverlist = [{'started_at': 1705967324.784141,
               'id': {'@type': 'pub.ed25519',
                      'key': 'lXOEbKr4hiiAi849AeY2S+z2W1Pgk0pzDgL3sLxkJRs='},
               'port': 30113,
               'ip': -957042655},
              {'started_at': 1705969782.036844,
               'id': {'@type': 'pub.ed25519',
                      'key': 'Fi6e++zdCQIYOoHze+i2ZzU8oKj6GbQIlya3GKVbLtQ='},
               'port': 30123,
               'ip': -957035708}]

lc = LiteClient(mode='roundrobin', my_rr_servers=serverlist)
start = lc.get_masterchain_info_ext()

mc_hashes = []


def process_mc(x):
    j, c = x

    lc = LiteClient(mode='roundrobin', my_rr_servers=serverlist,
                    timeout=10, num_try=5)
    answer = []
    for i in c:
        while True:
            try:
                block_id = lc.lookup_block(BlockId(-1, 0x8000000000000000, i)).blk_id

                current_full_block = lc.get_block(block_id)

                # It's stored in blockExtra
                block = Block().cell_unpack(current_full_block)
                block_info = BlockInfo().cell_unpack(block.info, True)
                block_extra = BlockExtra().cell_unpack(block.extra, False)

                rand_seed = int(block_extra.rand_seed, 2)
                prev_key_block_seqno = block_info.prev_key_block_seqno

                prev = block_info.prev_ref.prev
                prev_block = BlockIdExt(BlockId(block_id.id.workchain,
                                                block_id.id.shard,
                                                prev.seq_no),
                                        root_hash=int(prev.root_hash, 2),
                                        file_hash=int(prev.file_hash, 2))

                answer.append({
                    'block_id': block_id,
                    'shards': lc.get_all_shards_info(block_id),
                    'rand_seed': rand_seed,
                    'prev_key_block_seqno': prev_key_block_seqno
                })
                break
            except Exception as e:
                print(e)
                sleep(0.1)
    del lc
    return answer


mc_seqnos = list(enumerate(chunks(list(range(start.last.id.seqno - 700, start.last.id.seqno)), 50)))

with Pool(8) as pool:
    results = pool.imap_unordered(process_mc, mc_seqnos)

    for result in tqdm(results, desc="[multithread] Load blocks",
                       total=len(mc_seqnos)):
        mc_hashes.extend(result)

known_shards = []

for i in mc_hashes:
    known_shards.extend(i['shards'])

known_shards = set(known_shards)
print(len(known_shards))


def process_shard(x, prev_data=[]):
    global known_shards
    lc = LiteClient(mode='roundrobin', my_rr_servers=serverlist,
                    timeout=10, num_try=300)

    if isinstance(x, BlockId):
        block_id = lc.lookup_block(x).blk_id
    else:
        block_id = x
        x = x.id

    current_full_block = lc.get_block(block_id)

    # It's stored in blockExtra
    block = Block().cell_unpack(current_full_block)
    block_info = BlockInfo().cell_unpack(block.info, True)
    block_extra = BlockExtra().cell_unpack(block.extra, False)
    rand_seed = int(block_extra.rand_seed, 2)
    prev_key_block_seqno = block_info.prev_key_block_seqno
    right_shard = None

    if block_info.after_merge:
        left = block_info.prev_ref.prev1
        left_shard = BlockIdExt(BlockId(x.workchain,
                                        shard_child(x.shard, True),
                                        left.seq_no),
                                root_hash=int(left.root_hash, 2), file_hash=int(left.file_hash, 2))

        right = block_info.prev_ref.prev2
        right_shard = BlockIdExt(BlockId(x.workchain,
                                         shard_child(x.shard, False),
                                         right.seq_no),
                                 root_hash=int(right.root_hash, 2), file_hash=int(right.file_hash, 2))

        if left_shard.id not in known_shards:
            prev_data = [process_shard(left_shard), *prev_data]

        if right_shard.id not in known_shards:
            prev_data = [process_shard(right_shard), *prev_data]

    else:
        prev = block_info.prev_ref.prev
        left_shard = BlockIdExt(BlockId(x.workchain, x.shard, prev.seq_no),
                                root_hash=int(prev.root_hash, 2), file_hash=int(prev.file_hash, 2))

        if left_shard.id not in known_shards:
            data = [process_shard(left_shard), *prev_data]

    del lc
    return [{
        'block_id': block_id,
        'rand_seed': rand_seed,
        'prev_key_block_seqno': prev_key_block_seqno,
        'prev_block_left': left_shard,
        'preb_block_right': right_shard
    }, *prev_data]


for j in tqdm(list(known_shards)):
    process_shard(j)