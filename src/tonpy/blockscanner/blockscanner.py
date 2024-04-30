# Copyright (c) 2024 Disintar LLP Licensed under the Apache License Version 2.0

import math
import sys
import traceback
import typing
from collections import defaultdict

sys.path.append("../src")

import requests
import os
import signal

from tonpy import LiteClient, Cell, get_block_info, BlockId, BlockIdExt, \
    Address, Emulator, begin_cell, StackEntry, VmDict, CellSlice, SkipCryptoCurrency
from tonpy.tvm.not_native.emulator_extern import EmulatorExtern

from tonpy.utils.shard_account import shard_is_ancestor, shard_child, shard_parent
from tonpy.libs.python_ton import Bits256, globalSetVerbosity
from tonpy.autogen.block import Account, Transaction, Block, BlockInfo, BlockExtra, MessageAny, AccountState
from tonpy.utils.chunks import chunks
from multiprocessing import Pool, get_context
from time import sleep, time
from loguru import logger
import traceback as tb
from cytoolz import curry
import orjson as json
from tqdm import tqdm
from datetime import datetime
from typing import Callable, List
from threading import Thread
from queue import Queue
from multiprocessing import set_start_method

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
        # load accounts from block
        block_txs = block['account_blocks']
        del block['account_blocks']

        for account in block_txs:
            clear_tmp = []
            for x in block_txs[account]:
                if tx_subscriptions is None or tx_subscriptions.check(x['tx'].begin_parse()):
                    clear_tmp.append(x)
            block_txs[account] = clear_tmp
    else:
        # load accounts from LC
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
def load_process_blocks(blocks_chunk,
                        lcparams,
                        loglevel,
                        emulate_before_output,
                        tx_subscriptions):
    lcparams = json.loads(lcparams)
    lcparams['logprefix'] = 'blockprocessor'

    with LiteClient(**lcparams) as lc:
        blocks_txs = []

        if loglevel > 1:
            blocks_chunk = tqdm(blocks_chunk, desc="Load block TXs")

        for block in blocks_chunk:
            blocks_txs.extend(process_block(block, lc, emulate_before_output, tx_subscriptions))

    return blocks_txs


def process_shard(x, prev_data=None, lc=None, loglevel=None, known_shards=None, stop_shards=None,
                  parse_txs_over_ls=False, load_only_known=False):
    if loglevel > 2:
        data = f"Process shard call: {x}" \
               f"{len(prev_data) if prev_data is not None else ''}, " \
               f"Known shards: {len(known_shards)}, " \
               f"Stop shards: {len(stop_shards)}, "

        if loglevel > 3:
            my_seqno = x.seqno if isinstance(x, BlockId) else x.id.seqno

            old_min = -1
            old_type = 'known'
            for i in known_shards:
                if isinstance(i, BlockIdExt):
                    i = i.id

                if old_min < i.seqno < my_seqno:
                    old_min = i.seqno

            for i in stop_shards:
                if isinstance(i, BlockIdExt):
                    i = i.id

                if old_min < i.seqno < my_seqno:
                    old_min = i.seqno
                    old_type = 'stop'

            data += f" Nearest: {old_min} of type: {old_type}, it's {my_seqno - old_min} away"
        logger.info(data)

    if prev_data is None:
        prev_data = []

    if isinstance(x, BlockId):
        if loglevel > 2:
            logger.info(f"Call lookup block")

        block_id = lc.lookup_block(x).blk_id
    else:
        block_id = x
        x = x.id

    if loglevel > 2:
        logger.info(f"Call get block: {block_id}")

    current_full_block = lc.get_block(block_id)

    if loglevel > 2:
        logger.info(f"Got block: {block_id}")

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

        if not load_only_known and left_shard.id not in known_shards and block_id.id not in stop_shards:
            prev_data = [
                *process_shard(left_shard, lc=lc, prev_data=[], loglevel=loglevel, known_shards=known_shards,
                               stop_shards=stop_shards,
                               parse_txs_over_ls=parse_txs_over_ls), *prev_data]

        if not load_only_known and right_shard.id not in known_shards and block_id.id not in stop_shards:
            prev_data = [
                *process_shard(right_shard, lc=lc, prev_data=[], loglevel=loglevel, known_shards=known_shards,
                               stop_shards=stop_shards,
                               parse_txs_over_ls=parse_txs_over_ls), *prev_data]

    else:
        prev = block_info.prev_ref.prev

        if block_info.after_split:
            left_shard = BlockIdExt(BlockId(x.workchain, shard_parent(x.shard), prev.seq_no),
                                    root_hash=int(prev.root_hash, 2), file_hash=int(prev.file_hash, 2))
        else:
            left_shard = BlockIdExt(BlockId(x.workchain, x.shard, prev.seq_no),
                                    root_hash=int(prev.root_hash, 2), file_hash=int(prev.file_hash, 2))

        if not load_only_known and left_shard.id not in known_shards and block_id.id not in stop_shards:
            prev_data = [
                *process_shard(left_shard, lc=lc, prev_data=[], loglevel=loglevel, known_shards=known_shards,
                               stop_shards=stop_shards,
                               parse_txs_over_ls=parse_txs_over_ls), *prev_data]

    if loglevel > 2:
        logger.info(f"Done download shards")

    new_data = {
        'block_id': block_id,
        'rand_seed': rand_seed,
        'gen_utime': block_info.gen_utime,
        'prev_key_block_seqno': prev_key_block_seqno,
        'prev_block_left': left_shard,
        'prev_block_right': right_shard,
        'master': block_info.master_ref.master.seq_no,
        'account_blocks': convert_account_blocks_to_txs(
            block_extra.account_blocks) if not parse_txs_over_ls else None
    }

    return [new_data, *prev_data]


@curry
def load_process_shard_chunk(shards_chunk,
                             known_shards,
                             stop_shards,
                             lcparams,
                             loglevel,
                             parse_txs_over_ls=False,
                             load_only_known=False):
    thread_id, shards_chunk = shards_chunk

    if loglevel > 1:
        logger.info(f"Start thread: {thread_id}")

    try:
        total_start_at = time()
        answer = []

        lcparams = json.loads(lcparams)
        lcparams['logprefix'] = f'shards t{thread_id}'
        with LiteClient(**lcparams) as lc:
            if loglevel > 1:
                shards_chunk = tqdm(shards_chunk, desc=f"[shards t{thread_id}] Load shards")

            for shard in shards_chunk:
                start = None
                if loglevel > 3:
                    start = time()
                    logger.debug(f"[shards t{thread_id}] Call process shard: {shard}")

                answer.extend(
                    process_shard(shard, lc=lc, loglevel=loglevel,
                                  known_shards=known_shards, stop_shards=stop_shards,
                                  parse_txs_over_ls=parse_txs_over_ls, load_only_known=load_only_known))

                if loglevel > 3:
                    logger.debug(f"Done process shard: {shard} at {time() - start}")

            if loglevel > 3:
                logger.debug(f"[shards t{thread_id}] Stop liteclient")

        if loglevel > 3:
            logger.debug(f"[shards t{thread_id}] Finally done at: {time() - total_start_at}")

        return answer
    except Exception as e:
        logger.error(f"{e}")
        logger.error(f"{traceback.format_exc()}")
        return None


@curry
def process_mc_blocks(seqnos, lcparams, loglevel, parse_txs_over_ls):
    thread_id, seqnos = seqnos

    if loglevel > 2:
        logger.debug(f"[mc t{thread_id}] Start load MCs: {len(seqnos)}")

    lcparams = json.loads(lcparams)
    lcparams['logprefix'] = f'mcblocks t{thread_id}'

    if loglevel > 3:
        logger.debug(f"[mc t{thread_id}] Start LiteClient")

    try:
        with LiteClient(**lcparams) as lc:
            if loglevel > 3:
                logger.debug(f"[mc t{thread_id}] Started LiteClient")

            answer = []

            if loglevel > 1:
                seqnos = tqdm(seqnos, desc=f"mc t{thread_id} Load MCs")

            for i in seqnos:
                num_errs = 0

                while True:
                    try:
                        if loglevel > 2:
                            logger.debug(f"[{thread_id}] Ask block")

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

                        if loglevel > 3:
                            logger.debug(f"[mc t{thread_id}] ERROR in block: {e}")

                        if num_errs > 200:
                            logger.error(
                                f"Error in process_mc_blocks, block: (-1, 0x8000000000000000, {i}): {e}, {tb.format_exc()}")

                        if num_errs > 600:
                            raise e

                        sleep(0.1)

            if loglevel > 3:
                logger.debug(f"[mc t{thread_id}] Stop liteclient")

        if loglevel > 2:
            logger.debug(f"[mc t{thread_id}] Done load MCs")

        return answer
    except Exception as e:
        logger.error(f"[{thread_id}] Error {e}")
        logger.error(f"[{thread_id}] Error {traceback.format_exc()}")
        return None


class BlockScanner(Thread):
    def __init__(self,
                 lcparams: dict,
                 start_from: int = None,
                 load_to: int = None,
                 nproc: int = 20,
                 loglevel: int = 0,
                 raw_process: Callable = None,
                 chunk_size: int = 100,
                 tx_chunk_size: int = 5000,
                 out_queue: Queue = None,
                 only_mc_blocks: bool = False,
                 parse_txs_over_ls: bool = False,
                 transaction_subscriptions: "CustomSubscription" = None,
                 account_subscriptions: "CustomAccountSubscription" = None,
                 database_provider: "BaseDatabaseProvider" = None,
                 emulate_before_output: bool = None,
                 live_load_enable: bool = False,
                 load_chunks: typing.List[typing.Tuple[int, int]] = None,
                 allow_skip_mc_in_live: bool = True,
                 blocks_to_load: List[BlockIdExt] = None):
        """

        :param lcparams: Params for LiteClient
        :param start_from: Seqno of first block to load
        :param load_to: Seqno of last block to load
        :param nproc: Number of process
        :param loglevel: Logs: 0 - nothing, 1 - stats, 2 - tqdm
        :param chunk_size: Number of blocks to load to RAM per 1 iteration (depends on network load, number of process, available RAM)
        :param tx_chunk_size: Number of TXs that will be loaded to raw / emulate function per 1 iteration (better have a lot of blocks, but not much TXs for emulation per chunk)
        :param raw_process: Raw function to call on TXs in blocks (without emulation), will receive [block, account_state, txs]
        :param transaction_subscriptions: Rules to filter transactions that will be scanned
        :param account_subscriptions: Rules to filter accounts that will be scanned
        :param database_provider: TODO: Database connector to get information about accounts and states, save hashes, etc
        :param emulate_before_output: If True - will emulate transaction to get actual account state on TX, default False
        :param live_load_enable: If True - will load all new blocks, default False. If delta >90sec between updates - application will be killed
        :param load_chunks: [[start_from, load_to], ...] chunks to loads
        :param allow_skip_mc_in_live: if True - will load last known MC block after process chunk, if True - will load exactly NEXT MC seqno
        """
        super(BlockScanner, self).__init__()

        try:
            set_start_method("spawn")
        except RuntimeError:
            logger.warning(f"Multiprocess context already set(?)")

        self.load_specific = False
        self.mc_to_load = []
        self.shards_to_load = []

        if blocks_to_load is not None:
            if start_from is not None or load_to is not None:
                raise ValueError(f"blocks_to_load and start_from/load_to is not compatible")

            self.load_specific = True

            for block in blocks_to_load:
                if block.id.workchain == -1:
                    self.mc_to_load.append(block.id.seqno)
                else:
                    self.shards_to_load.append(block)

        self.only_mc_blocks = only_mc_blocks
        self.lcparams = json.dumps(lcparams)
        lcparams['logprefix'] = f'main'
        self.lc = LiteClient(**lcparams)
        lcparams['timeout'] = 200
        lcparams['logprefix'] = f'main longterm'
        self.lc_long = LiteClient(**lcparams)
        self.start_from = start_from
        self.load_chunks = load_chunks

        if self.start_from is None and self.load_chunks is not None:
            self.start_from = self.load_chunks[0][0]
            load_to = self.load_chunks[0][1]
            self.load_chunks = self.load_chunks[1:]
        elif self.start_from is None and not self.load_specific:
            raise ValueError("Provide start_from or load_chunks")

        self.live_load_enable = live_load_enable

        if load_to is not None:
            self.load_to = load_to

            if self.live_load_enable:
                logger.info("Live load and load_to enabled (?)")
        else:
            if not self.live_load_enable and not self.load_specific:
                raise ValueError(f"Provide load_to or live_load_enable")

            self.load_to = self.lc.get_masterchain_info_ext().last.id.seqno

        if self.live_load_enable:
            self.allow_skip_mc_in_live = allow_skip_mc_in_live

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
        if from_ is None and not self.load_specific:
            raise ValueError(f"self.load_specific must be True")

        if self.load_specific and len(self.mc_to_load) == 0:
            return []

        mc_data = []

        if not self.load_specific:
            blocks_ids = list(range(from_, to_))
        else:
            blocks_ids = self.mc_to_load

        mc_seqnos_chunks, p = self.detect_cs_p(blocks_ids)

        with get_context("spawn").Pool(p) as pool:
            results = pool.imap_unordered(process_mc_blocks(lcparams=self.lcparams, loglevel=self.loglevel,
                                                            parse_txs_over_ls=self.parse_txs_over_ls),
                                          enumerate(mc_seqnos_chunks))

            if self.loglevel > 1:
                results = tqdm(results, desc="Download MC blocks", total=len(mc_seqnos_chunks))

            for result in results:
                if result is None:
                    raise ValueError(f"Invalid result in MC blocks")
                mc_data.extend(result)

        # for i in tqdm(enumerate(mc_seqnos_chunks), total=len(mc_seqnos_chunks)):
        #     mc_data.extend(process_mc_blocks(i, lcparams=self.lcparams, loglevel=self.loglevel,
        #                                      parse_txs_over_ls=self.parse_txs_over_ls))

        # todo: check hashes
        return mc_data

    def load_process_shard(self, known_shards, stop_shards):
        shards_data = []

        if self.load_specific:
            if len(self.shards_to_load) == 0:
                return []

            known_shards = self.shards_to_load

        known_shards_chunks, p = self.detect_cs_p(list(known_shards))

        if self.loglevel > 2:
            logger.debug(f"Start {p} processes with {len(known_shards_chunks)} chunks with {len(known_shards)}")

        with get_context("spawn").Pool(p) as pool:
            results = pool.imap_unordered(
                load_process_shard_chunk(known_shards=known_shards, stop_shards=stop_shards, lcparams=self.lcparams,
                                         loglevel=self.loglevel, parse_txs_over_ls=self.parse_txs_over_ls,
                                         load_only_known=self.load_specific),
                enumerate(known_shards_chunks))

            if self.loglevel > 1:
                results = tqdm(results, desc=f"Download shards / {p}", total=len(known_shards_chunks))

            for result in results:
                if result is None:
                    raise ValueError(f"Invalid result in shards process")
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
        if self.emulate_before_output:
            known_mcs = {}

            for i in mc_data:
                known_mcs[i['block_id'].id.seqno] = i['block_id']

            to_load_masters = []

            if len(known_mcs.keys()) > 0:
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
        else:
            for x in mc_data:
                x['prev_block_data'] = []
                x['prev_block_left'] = None
                x['prev_block_right'] = None
                x['key_block'] = self.known_key_blocks[x['prev_key_block_seqno']]

            for x in shards_data:
                x['prev_block_data'] = []
                x['prev_block_left'] = None
                x['prev_block_right'] = None
                x['key_block'] = self.known_key_blocks[x['prev_key_block_seqno']]

        return shards_data, mc_data

    def load_process_blocks(self, blocks, tx_subscriptions=None):
        txs_data = []
        blocks_chunks, p = self.detect_cs_p(list(blocks))

        with get_context("spawn").Pool(p) as pool:
            results = pool.imap_unordered(load_process_blocks(lcparams=self.lcparams, loglevel=self.loglevel,
                                                              emulate_before_output=self.emulate_before_output,
                                                              tx_subscriptions=tx_subscriptions),
                                          blocks_chunks)

            if self.loglevel > 1:
                results = tqdm(results, desc="Download TXs", total=len(blocks_chunks))

            for result in results:
                txs_data.extend(result)

        return txs_data

    def load_historical(self):
        stop = False
        start_from = self.start_from
        while not stop:
            if self.loglevel > 1:
                logger.debug(f"Start load historical from seqno: {start_from}")

            started_at = time()
            mc_start_at = time()

            end_at = None

            if self.load_specific or (start_from + self.chunk_size >= self.load_to):
                end_at = self.load_to

                if self.loglevel > 1:
                    logger.debug(f"Start load master from seqno: {start_from} to {end_at}")

                mc_data = self.load_mcs(start_from, self.load_to)
                stop = True

                if self.loglevel > 1:
                    logger.debug(
                        f"End load LAST master chunk from seqno: {start_from} to {end_at} at {time() - mc_start_at}")

                if not self.load_specific:
                    stop_shards = self.lc.get_all_shards_info(
                        self.lc.lookup_block(BlockId(-1, 0x8000000000000000, start_from - 1)).blk_id
                    )
                else:
                    stop_shards = []
            else:
                end_at = start_from + self.chunk_size

                if self.loglevel > 1:
                    logger.debug(f"Start load master from seqno: {start_from} to {end_at}")

                mc_data = self.load_mcs(start_from, end_at)

                if self.loglevel > 1:
                    logger.debug(
                        f"End load master chunk from seqno: {start_from} to {end_at} at {time() - mc_start_at}")

                stop_shards = self.lc.get_all_shards_info(
                    self.lc.lookup_block(BlockId(-1, 0x8000000000000000, start_from - 1)).blk_id
                )
                start_from += self.chunk_size
            mc_hashes = list(sorted(mc_data, key=lambda x: x['block_id'].id.seqno))

            if self.loglevel > 1:
                logger.debug(f"End load historical MASTER to seqno: {end_at}, ask stop_shards")

            if self.loglevel > 1:
                logger.debug(f"Got: {len(stop_shards)} stop shards")

            known_shards = []

            if not self.load_specific:
                for i in mc_hashes:
                    known_shards.extend(i['shards'])

            known_shards = set(known_shards)
            mc_end_at = time() - mc_start_at

            if self.loglevel > 1:
                logger.debug(f"Total mc download ended at: {mc_end_at}, start download shards")

            shards_start_at = time()
            if not self.only_mc_blocks:
                # maybe better not to sort but force shuffle to distribute load
                shards_data = self.load_process_shard(known_shards=list(sorted(known_shards, key=lambda x: x.seqno)),
                                                      stop_shards=stop_shards)

                if self.loglevel > 1:
                    logger.debug(f"Shards downloaded at: {time() - shards_start_at}")
            else:
                if self.loglevel > 1:
                    logger.debug(f"Loading only MC data, skip")

                shards_data = []
            shards_end_at = time() - shards_start_at

            key_blocks_start_at = time()

            if self.loglevel > 1:
                logger.debug(f"Start download key blocks")

            self.prepare_key_blocks(shards_data, mc_data)

            if self.loglevel > 1:
                logger.debug(f"Downloaded key blocks: {time() - key_blocks_start_at}")

            shards_data, mc_data = self.prepare_prev_block_data(shards_data, mc_data)

            if self.loglevel > 1:
                logger.debug(f"End getting prev blocks at: {time() - key_blocks_start_at}")

            key_blocks_end_at = time() - key_blocks_start_at

            if self.emulate_before_output:
                mega_libs_start_at = time()

                if self.loglevel > 1:
                    logger.debug(f"Start get mega libs: {time() - key_blocks_start_at}")

                mega_libs = get_mega_libs()

                for i in shards_data:
                    i['libs'] = mega_libs

                for j in mc_data:
                    j['libs'] = mega_libs
                mega_libs_end_at = time() - mega_libs_start_at

                if self.loglevel > 1:
                    logger.debug(f"Mega libs downloaded at: {mega_libs_end_at}")
            else:
                if self.loglevel > 1:
                    logger.debug(f"Skip mega libs download")

                mega_libs_start_at = time()
                mega_libs_end_at = time() - mega_libs_start_at

            process_block_start_at = time()

            if self.loglevel > 1:
                logger.debug(f"Start download and process transactions")

            # [block, account_state, txs]
            txs = self.load_process_blocks(mc_data + shards_data, tx_subscriptions=self.transaction_subscriptions)

            process_block_end_at = time() - process_block_start_at

            if self.loglevel > 1:
                logger.debug(f"End download and process transactions at: {process_block_end_at}")

            if self.loglevel > 0:
                gen_utimes = [datetime.fromtimestamp(i['gen_utime']) for i in mc_data + shards_data]
                seqnos = [i['block_id'].id.seqno for i in mc_data + shards_data]

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
                if self.loglevel > 1:
                    logger.debug(f"Put transactions to output and continue to next chunk, stop: {stop}")

                self.out_queue.put({
                    'seqno': end_at,
                    'txs': txs
                })

                if self.loglevel > 3:
                    logger.debug(f"Data put, go")
                continue

            start_emulate_at = time()
            if self.loglevel > 1:
                logger.debug(f"We have raw process function - start process")

            tmp = list(chunks(txs, self.tx_chunk_size))

            if self.loglevel > 1:
                tmp = tqdm(tmp, desc="Process raw", total=len(tmp))

            if not self.process_raw:
                self.f = process_subscriptions(tx_subscriptions=self.transaction_subscriptions,
                                               account_subscriptions=self.account_subscriptions)

            total = len(tmp)

            for chunk_no, c in enumerate(tmp):
                if self.loglevel > 1:
                    logger.debug(f"Process chunk №{chunk_no} / {total}, {len(c)}")

                with get_context("spawn").Pool(self.nproc) as pool:
                    results = pool.imap_unordered(self.f, c, chunksize=max(300, math.ceil(len(c) / self.nproc)))

                    for result_chunk in results:
                        if len(result_chunk) > 0:
                            self.out_queue.put(result_chunk)

            if self.loglevel > 0:
                logger.info(f"\n\tProcessed TXs at: {time() - start_emulate_at}")

    def run(self):
        try:
            if self.loglevel > 1:
                logger.debug("Start load historical")

            self.load_historical()

            if self.load_chunks is not None and len(self.load_chunks) > 0:
                if self.loglevel > 1:
                    logger.debug("Start load other chunks")

                for c in self.load_chunks:
                    self.start_from = c[0]
                    self.load_to = c[1]
                    self.load_historical()

            self.done = True

            if self.live_load_enable:
                if self.loglevel > 1:
                    logger.debug("Start load live data")

                self.load_live()
            elif self.loglevel > 1:
                logger.debug("End of loading")
        except Exception as e:
            self.out_queue.put(e)
            raise e

    def load_live(self):
        last_update = datetime.now()

        while True:
            try:
                self.start_from = self.load_to

                # Get last block seqno from MC
                self.load_to = self.lc_long.wait_masterchain_seqno(self.load_to + 1, 10000).last.id.seqno

                self.load_historical()
                last_update = datetime.now()

            except Exception as e:
                delta = (datetime.now() - last_update).total_seconds()
                logger.error(f"Error in live load: {e}, retry. Delta: {delta}")

                if delta > 80:
                    logger.error(f"Fatal error, too big delta: {delta}")
                    self.out_queue.put(ValueError("Delta too big"))
                    os.kill(os.getpid(), signal.SIGKILL)  # todo: remove?


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
