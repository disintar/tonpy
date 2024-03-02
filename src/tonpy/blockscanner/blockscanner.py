# Copyright (c) 2024 Disintar LLP Licensed under the Apache License Version 2.0

import math
import sys
import traceback
import typing
from collections import defaultdict

sys.path.append("../src")

import requests

from tonpy import LiteClient, Cell, get_block_info, BlockId, BlockIdExt, \
    Address, Emulator, begin_cell, StackEntry, VmDict, CellSlice, SkipCryptoCurrency
from tonpy.tvm.not_native.emulator_extern import EmulatorExtern

from tonpy.utils.shard_account import shard_is_ancestor, shard_child, shard_parent
from tonpy.libs.python_ton import Bits256, globalSetVerbosity
from tonpy.autogen.block import Account, Transaction, Block, BlockInfo, BlockExtra, MessageAny, AccountState
from tonpy.utils.chunks import chunks
from multiprocessing import Pool
from time import sleep, time
from loguru import logger
import traceback as tb
from toolz import curry
import orjson as json
from tqdm import tqdm
from datetime import datetime
from typing import Callable
from threading import Thread
from queue import Queue

globalSetVerbosity(-1)

if typing.TYPE_CHECKING:
    from tonpy.blockscanner import CustomSubscription, CustomAccountSubscription
    from tonpy.blockscanner.database_provider import BaseDatabaseProvider


def convert_account_blocks_to_txs(account_blocks_all):
    block_txs = {}

    r: CellSlice = account_blocks_all.begin_parse()

    if r.refs > 0:
        account_blocks = VmDict(256, False, cell_root=r.load_ref(),
                                aug=SkipCryptoCurrency())
    else:
        account_blocks = []

    for i in account_blocks:
        account, data = i
        data = data.data
        # acc_trans#5
        assert data.load_uint(4) == 5
        me = data.load_uint(256)

        # account_addr:bits256
        assert me == account

        # state_update:^(HASH_UPDATE Account)
        data.skip_refs(1, True)

        transactions = VmDict(64, False, cell_root=data, aug=SkipCryptoCurrency())

        for t in transactions:
            lt, txdata = t
            tx = txdata.data.load_ref()
            tx_tlb = Transaction()
            tx_tlb = tx_tlb.cell_unpack(tx, True)

            account_address = int(tx_tlb.account_addr, 2)
            assert account_address == me

            if account_address not in block_txs:
                block_txs[account_address] = []

            block_txs[account_address].append({
                'tx': tx,
                'lt': tx_tlb.lt,
                'now': tx_tlb.now,
                'account': account_address,
                'is_tock': tx_tlb.description.is_tock if hasattr(tx_tlb.description, 'is_tock') else False
            })

    return block_txs


@curry
def process_subscriptions(data,
                          tx_subscriptions: "CustomSubscription" = None,
                          account_subscriptions: "CustomAccountSubscription" = None):
    block, account_state, txs = data

    # todo: get 1 tx, get account and pass over account_subscriptions

    if account_state is None:
        if tx_subscriptions is not None:
            txs = [[block['block_id'], i] for i in list(filter(tx_subscriptions.check, [tx['tx'] for tx in txs]))]
        else:
            txs = [[block['block_id'], i['tx']] for i in txs]
        return txs
    else:
        # todo: emulate all transactions & process each over account_subscriptions and tx_subscriptions
        raise NotImplementedError("Emulation not supported yet")


def get_mega_libs(num_try=100):
    cur = 0

    while cur < num_try:
        try:
            query = '''query{mega_libs_cell}'''
            response = requests.post("https://dton.io/graphql", json={'query': query})
            return response.json()['data']['mega_libs_cell']
        except Exception as e:
            logger.error(f"Can't get dton.io/graphql: {e}, {tb.format_exc()}")
            sleep(0.1)
            cur += 1


def process_block(block, lc, emulate_before_output, tx_subscriptions):
    block_txs = {}

    if block['account_blocks'] is not None:
        block_txs = block['account_blocks']
        del block['account_blocks']

        for account in block_txs:
            clear_tmp = []
            for x in block_txs[account]:
                if tx_subscriptions is None or tx_subscriptions.check(x['tx'].begin_parse()):
                    clear_tmp.append(x)
            block_txs[account] = clear_tmp
    else:
        ready = False

        account_address = None
        lt = None

        while not ready:
            answer = lc.list_block_transactions_ext(block['block_id'], 256,
                                                    account_address=account_address,
                                                    lt=lt)
            ready = not answer.incomplete

            for tx in answer.transactions:
                if tx_subscriptions is not None:
                    if not tx_subscriptions.check(tx.begin_parse()):
                        continue

                tx_tlb = Transaction()
                tx_tlb = tx_tlb.cell_unpack(tx, True)

                account_address = int(tx_tlb.account_addr, 2)

                if account_address not in block_txs:
                    block_txs[account_address] = []

                block_txs[account_address].append({
                    'tx': tx,
                    'lt': tx_tlb.lt,
                    'now': tx_tlb.now,
                    'is_tock': tx_tlb.description.is_tock if hasattr(tx_tlb.description, 'is_tock') else False
                })

                lt = tx_tlb.lt

    total_block_txs = []

    for account in block_txs:
        if emulate_before_output:
            address_acc = f"{block['block_id'].id.workchain}:{hex(account).upper()[2:].zfill(64)}"
            acc = Address(address_acc)

            if shard_is_ancestor(block['prev_block_left'].id.shard,
                                 acc.shard_prefix(60)):
                state_block = block['prev_block_left']
            else:
                state_block = block['prev_block_right']

            # Load account state from prev block
            account_state = lc.get_account_state(acc, state_block)

            if not account_state.root.is_null():
                # Convert answer to AccountShardState
                account_state = begin_cell() \
                    .store_ref(account_state.root) \
                    .store_uint(int(account_state.last_trans_hash, 16), 256) \
                    .store_uint(account_state.last_trans_lt, 64).end_cell()
            else:
                account_state = begin_cell() \
                    .store_ref(begin_cell().store_uint(0, 1).end_cell()) \
                    .store_uint(int(account_state.last_trans_hash, 16), 256) \
                    .store_uint(account_state.last_trans_lt, 64) \
                    .end_cell()
        else:
            account_state = None

        total_block_txs.append([block, account_state, block_txs[account]])

    return total_block_txs


@curry
def load_process_blocks(blocks_chunk, lcparams, loglevel, emulate_before_output, tx_subscriptions):
    lcparams = json.loads(lcparams)
    lc = LiteClient(**lcparams)

    blocks_txs = []

    if loglevel > 1:
        blocks_chunk = tqdm(blocks_chunk, desc="Load block TXs")

    for block in blocks_chunk:
        blocks_txs.extend(process_block(block, lc, emulate_before_output, tx_subscriptions))

    return blocks_txs


@curry
def load_process_shard(shards_chunk,
                       known_shards,
                       stop_shards,
                       lcparams,
                       loglevel,
                       parse_txs_over_ls=False):
    answer = []

    lcparams = json.loads(lcparams)
    lc = LiteClient(**lcparams)

    def process_shard(x, prev_data=None, lc=None):
        if prev_data is None:
            prev_data = []

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

            if left_shard.id not in known_shards and block_id.id not in stop_shards:
                prev_data = [*process_shard(left_shard, lc=lc, prev_data=[]), *prev_data]

            if right_shard.id not in known_shards and block_id.id not in stop_shards:
                prev_data = [*process_shard(right_shard, lc=lc, prev_data=[]), *prev_data]

        else:
            prev = block_info.prev_ref.prev

            if block_info.after_split:
                left_shard = BlockIdExt(BlockId(x.workchain, shard_parent(x.shard), prev.seq_no),
                                        root_hash=int(prev.root_hash, 2), file_hash=int(prev.file_hash, 2))
            else:
                left_shard = BlockIdExt(BlockId(x.workchain, x.shard, prev.seq_no),
                                        root_hash=int(prev.root_hash, 2), file_hash=int(prev.file_hash, 2))

            if left_shard.id not in known_shards and block_id.id not in stop_shards:
                prev_data = [*process_shard(left_shard, lc=lc, prev_data=[]), *prev_data]

        del lc
        return [{
            'block_id': block_id,
            'rand_seed': rand_seed,
            'gen_utime': block_info.gen_utime,
            'prev_key_block_seqno': prev_key_block_seqno,
            'prev_block_left': left_shard,
            'prev_block_right': right_shard,
            'master': block_info.master_ref.master.seq_no,
            'account_blocks': convert_account_blocks_to_txs(
                block_extra.account_blocks) if not parse_txs_over_ls else None
        }, *prev_data]

    if loglevel > 1:
        shards_chunk = tqdm(shards_chunk, desc="Load shards")

    for shard in shards_chunk:
        answer.extend(process_shard(shard, lc=lc))

    return answer


@curry
def process_mc_blocks(seqnos, lcparams, loglevel, parse_txs_over_ls):
    lcparams = json.loads(lcparams)
    lc = LiteClient(**lcparams)

    answer = []

    if loglevel > 1:
        seqnos = tqdm(seqnos, desc="Load MCs")

    for i in seqnos:
        num_errs = 0

        while True:
            try:
                block_id = lc.lookup_block(BlockId(-1, 0x8000000000000000, i)).blk_id
                current_full_block = lc.get_block(block_id)
                block = Block().cell_unpack(current_full_block)
                block_info = BlockInfo().cell_unpack(block.info, True)
                block_extra = BlockExtra().cell_unpack(block.extra, False)

                rand_seed = int(block_extra.rand_seed, 2)
                prev_key_block_seqno = block_info.prev_key_block_seqno

                # todo: add prev hash

                answer.append({
                    'block_id': block_id,
                    'shards': lc.get_all_shards_info(block_id),
                    'rand_seed': rand_seed,
                    'gen_utime': block_info.gen_utime,
                    'prev_key_block_seqno': prev_key_block_seqno,
                    'gen_utime': block_info.gen_utime,
                    'account_blocks': convert_account_blocks_to_txs(
                        block_extra.account_blocks) if not parse_txs_over_ls else None
                })

                break
            except Exception as e:
                num_errs += 1
                if num_errs > 600:
                    logger.error(
                        f"Error in process_mc_blocks, block: (-1, 0x8000000000000000, {i}): {e}, {tb.format_exc()}")

                if num_errs > 3000:
                    raise e

                sleep(0.1)
    del lc
    return answer


class BlockScanner(Thread):
    def __init__(self,
                 lcparams: dict,
                 start_from: int,
                 load_to: int,
                 nproc: int = 20,
                 loglevel: int = 0,
                 raw_process: Callable = None,
                 chunk_size: int = 1000,
                 tx_chunk_size: int = 40000,
                 out_queue: Queue = None,
                 only_mc_blocks: bool = False,
                 parse_txs_over_ls: bool = False,
                 transaction_subscriptions: "CustomSubscription" = None,
                 account_subscriptions: "CustomAccountSubscription" = None,
                 database_provider: "BaseDatabaseProvider" = None,
                 emulate_before_output: bool = None):
        """

        :param lcparams: Params for LiteClient
        :param start_from: Seqno of first block to load
        :param load_to: Seqno of last block to load
        :param nproc: Number of process
        :param loglevel: Logs: 0 - nothing, 1 - stats, 2 - tqdm
        :param chunk_size: Number of blocks to load to RAM per 1 iteration (depends on network load, number of process, available RAM)
        :param tx_chunk_size: Number of TXs that will be loaded to raw / emulate function per 1 iteration. 40k is good option by default, if you have <32gb ram consider to low this value
        :param raw_process: Raw function to call on TXs in blocks (without emulation), will receive [block, account_state, txs]
        :param transaction_subscriptions: Rules to filter transactions that will be scanned
        :param account_subscriptions: Rules to filter accounts that will be scanned
        :param database_provider: TODO: Database connector to get information about accounts and states, save hashes, etc
        :param emulate_before_output: If True - will emulate transaction to get actual account state on TX, default False
        """
        super(BlockScanner, self).__init__()

        self.only_mc_blocks = only_mc_blocks
        self.lcparams = json.dumps(lcparams)
        self.lc = LiteClient(**lcparams)
        self.start_from = start_from
        self.load_to = load_to
        self.loglevel = loglevel
        self.nproc = nproc
        self.chunk_size = chunk_size
        self.out_queue = out_queue
        self.parse_txs_over_ls = parse_txs_over_ls
        self.tx_chunk_size = tx_chunk_size
        self.transaction_subscriptions = transaction_subscriptions
        self.account_subscriptions = account_subscriptions
        self.emulate_before_output = emulate_before_output
        self.known_key_blocks = {}
        self.mega_libs = get_mega_libs()

        self.process_raw = raw_process is not None
        if self.process_raw:
            self.f = raw_process
            assert out_queue is not None
            assert self.transaction_subscriptions is None, "Can't use transaction_subscription with process_raw"
            assert self.account_subscriptions is None, "Can't use account_subscriptions with process_raw"
            assert database_provider is None, "Can't use database_provider with process_raw"
            assert self.emulate_before_output is None, "Can't use emulate_before_output with process_raw"
            self.emulate_before_output = True
        else:
            self.f = None

            if self.emulate_before_output is None:
                self.emulate_before_output = False

        self.done = False

    def detect_cs_p(self, list_):
        cs = max(1, math.ceil(len(list_) / self.nproc))
        list_ = list(chunks(list_, cs))
        p = min(self.nproc, len(list_))
        return list_, p

    def load_mcs(self, from_, to_):
        mc_data = []
        blocks_ids = list(range(from_, to_))
        mc_seqnos_chunks, p = self.detect_cs_p(blocks_ids)

        with Pool(p) as pool:
            results = pool.imap_unordered(process_mc_blocks(lcparams=self.lcparams, loglevel=self.loglevel,
                                                            parse_txs_over_ls=self.parse_txs_over_ls),
                                          mc_seqnos_chunks)

            for result in results:
                mc_data.extend(result)
        # todo: check hashes
        return mc_data

    def load_process_shard(self, known_shards, stop_shards):
        shards_data = []
        known_shards_chunks, p = self.detect_cs_p(list(known_shards))

        with Pool(p) as pool:
            results = pool.imap_unordered(
                load_process_shard(known_shards=known_shards, stop_shards=stop_shards, lcparams=self.lcparams,
                                   loglevel=self.loglevel, parse_txs_over_ls=self.parse_txs_over_ls),
                known_shards_chunks)

            for result in results:
                shards_data.extend(result)

        return shards_data

    def prepare_key_blocks(self, shards_data, mc_data):
        # find all key blocks
        keys = []

        for i in shards_data + mc_data:
            keys.append(i['prev_key_block_seqno'])

        def get_key_block(x):
            blk_id, config = self.lc.get_config_all(
                self.lc.lookup_block(BlockId(-1, 0x8000000000000000, x)).blk_id,
                from_not_trusted_keyblock=True)

            config = config.get_cell().copy()
            return {
                'blk_id': blk_id,
                'config': config
            }

        key_blocks = list(set(keys))

        if self.loglevel > 1:
            key_blocks = tqdm(key_blocks, desc="Load key blocks")

        for i in key_blocks:
            self.known_key_blocks[i] = get_key_block(i)

    def prepare_prev_block_data(self, shards_data, mc_data):
        known_mcs = {}

        for i in mc_data:
            known_mcs[i['block_id'].id.seqno] = i['block_id']

        to_load_masters = []

        last_mc = min(known_mcs.keys())

        for i in range(last_mc - 16, last_mc):
            to_load_masters.append(i)

        for s in shards_data:
            for i in range(s['master'] - 15, s['master'] + 1):
                if i not in known_mcs:
                    to_load_masters.append(i)

        to_load_masters = list(set(to_load_masters))

        if self.loglevel > 1:
            to_load_masters = tqdm(to_load_masters, desc="Load prev data")

        for x in to_load_masters:
            known_mcs[x] = self.lc.lookup_block(BlockId(-1, 0x8000000000000000, x)).blk_id

        known_prev_block_data = {}

        for x in mc_data:
            prev_blocks = []

            for i in range(x['block_id'].id.seqno - 16, x['block_id'].id.seqno):
                prev_blocks.append(known_mcs[i].to_data())

            prev_blocks = list(reversed(prev_blocks))
            key = self.known_key_blocks[x['prev_key_block_seqno']]
            x['prev_block_data'] = [prev_blocks, key['blk_id'].to_data()]
            x['prev_block_left'] = known_mcs[i]
            x['prev_block_right'] = None
            x['key_block'] = key
            known_prev_block_data[x['block_id'].id.seqno] = x['prev_block_data']

        for i in shards_data:
            i['master'] += 1

            key = self.known_key_blocks[i['prev_key_block_seqno']]
            i['key_block'] = key

            if i['master'] in known_prev_block_data:
                i['prev_block_data'] = known_prev_block_data[i['master']]
            else:
                prev_blocks = []
                for j in range(i['master'] - 16, i['master']):
                    prev_blocks.append(known_mcs[j].to_data())

                prev_blocks = list(reversed(prev_blocks))
                i['prev_block_data'] = [prev_blocks, key['blk_id'].to_data()]
                known_prev_block_data[i['master']] = i['prev_block_data']

            i['master'] -= 1

        return shards_data, mc_data

    def load_process_blocks(self, blocks, tx_subscriptions=None):
        txs_data = []
        blocks_chunks, p = self.detect_cs_p(list(blocks))

        with Pool(p) as pool:
            results = pool.imap_unordered(load_process_blocks(lcparams=self.lcparams, loglevel=self.loglevel,
                                                              emulate_before_output=self.emulate_before_output,
                                                              tx_subscriptions=tx_subscriptions),
                                          blocks_chunks)

            for result in results:
                txs_data.extend(result)

        return txs_data

    def load_historical(self):
        stop = False
        start_from = self.start_from
        while not stop:
            started_at = time()

            mc_start_at = time()
            if start_from + self.chunk_size >= self.load_to:
                mc_data = self.load_mcs(start_from, self.load_to)
                stop = True
            else:
                mc_data = self.load_mcs(start_from, start_from + self.chunk_size)
                start_from += self.chunk_size

            mc_hashes = list(sorted(mc_data, key=lambda x: x['block_id'].id.seqno))
            stop_shards = mc_hashes[0]['shards']

            known_shards = []

            for i in mc_hashes:
                known_shards.extend(i['shards'])

            known_shards = set(known_shards)
            mc_end_at = time() - mc_start_at

            shards_start_at = time()
            if not self.only_mc_blocks:
                shards_data = self.load_process_shard(known_shards=known_shards, stop_shards=stop_shards)
            else:
                shards_data = []
            shards_end_at = time() - shards_start_at

            key_blocks_start_at = time()
            self.prepare_key_blocks(shards_data, mc_data)

            shards_data, mc_data = self.prepare_prev_block_data(shards_data, mc_data)
            key_blocks_end_at = time() - key_blocks_start_at

            if self.emulate_before_output:
                mega_libs_start_at = time()
                mega_libs = get_mega_libs()

                for i in shards_data:
                    i['libs'] = mega_libs

                for j in mc_data:
                    j['libs'] = mega_libs
                mega_libs_end_at = time() - mega_libs_start_at
            else:
                mega_libs_start_at = time()
                mega_libs_end_at = time() - mega_libs_start_at

            process_block_start_at = time()

            # [block, account_state, txs]
            # if self.emulate_before_output:
            txs = self.load_process_blocks(mc_data + shards_data, tx_subscriptions=self.transaction_subscriptions)
            # else:
            #     txs = []
            #
            #     for block in mc_data + shards_data:
            #         tmp = block['account_blocks']
            #         del block['account_blocks']
            #
            #         for account in tmp:
            #             clear_tmp = []
            #             for x in tmp[account]:
            #                 if self.transaction_subscriptions is None or \
            #                         self.transaction_subscriptions.check(x['tx'].begin_parse()):
            #                     clear_tmp.append(x)
            #
            #             if len(clear_tmp):
            #                 txs.append([block, None, clear_tmp])
            #
            #     if len(txs):
            #         self.out_queue.put(txs)

            process_block_end_at = time() - process_block_start_at

            if self.loglevel > 0:
                gen_utimes = [datetime.fromtimestamp(i['gen_utime']) for i in mc_data]
                seqnos = [i['block_id'].id.seqno for i in mc_data]

                start_block_gen_utime = min(gen_utimes)
                end_block_gen_utime = max(gen_utimes)

                start_block_seqno = min(seqnos)
                end_block_seqno = max(seqnos)

                logger.info(
                    f"\n\nStats, loaded:\n\t{len(mc_data)} MC blocks\n\t{len(shards_data)} shard blocks"
                    f"\n\t{sum([len(i[-1]) for i in txs])} TXs\n\tMin/max MC gen_utime: {start_block_gen_utime} / {end_block_gen_utime} "
                    f"  : Loaded time {end_block_gen_utime - start_block_gen_utime}"
                    f"\n\tMin/max MC seqnos: {start_block_seqno} / {end_block_seqno} "
                    f": Loaded seqnos {end_block_seqno - start_block_seqno}"
                    f"\n\tLoaded at: {time() - started_at}, MC at: {mc_end_at}, Shards at: {shards_end_at},"
                    f"\n\tKey at: {key_blocks_end_at}, Libs at: {mega_libs_end_at}, TXs at: {process_block_end_at}\n\n"
                    f"\n\tChunks count: {len(txs)}, {sum([len(i[2]) for i in txs])} TXs")

            if not self.emulate_before_output:
                continue

            start_emulate_at = time()
            tmp = list(chunks(txs, self.tx_chunk_size))

            if self.loglevel > 1:
                tmp = tqdm(tmp, desc="Process raw", total=len(tmp))

            if not self.process_raw:
                self.f = process_subscriptions(tx_subscriptions=self.transaction_subscriptions,
                                               account_subscriptions=self.account_subscriptions)

            for c in tmp:
                with Pool(self.nproc) as pool:
                    results = pool.imap_unordered(self.f, c, chunksize=max(300, math.ceil(len(c) / self.nproc)))

                    for result_chunk in results:
                        if len(result_chunk) > 0:
                            self.out_queue.put(result_chunk)

            if self.loglevel > 0:
                logger.info(f"\n\tProcessed TXs at: {time() - start_emulate_at}")

    def run(self):
        self.load_historical()
        self.done = True


def raw_process(chunk):
    out = []

    for data in chunk:
        block, state, txs = data
        out.append(len(txs))
    return out


if __name__ == "__main__":
    lcparams = {
        'mode': 'roundrobin',
        'my_rr_servers': [],
        'timeout': 1,
        'num_try': 3000,
        'threads': 1
    }

    outq = Queue()

    scanner = BlockScanner(
        lcparams=lcparams,
        start_from=35381340,
        load_to=35381340 + 2,
        nproc=10,
        loglevel=2,
        chunk_size=2,
        raw_process=raw_process,
        out_queue=outq,
        only_mc_blocks=True,
        parse_txs_over_ls=True
    )

    scanner.start()

    while not scanner.done:
        print("Not done, wait")
        sleep(10)

    total_txs = 0
    while not outq.empty():
        for result in outq.get():
            total_txs += result
    print("Got total: ", total_txs)
