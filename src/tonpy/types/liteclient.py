# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0
import datetime
import random
import traceback
from typing import Union, TYPE_CHECKING, Tuple, List, Optional
from types import MethodType

from loguru import logger
from tonpy.libs.python_ton import PyLiteClient, ipv4_int_to_str, globalSetVerbosity, BlockId as ton_BlockId, \
    BlockIdExt as ton_BlockIdExt

from tonpy.types.cell import Cell
from tonpy.types.address import Address

from tonpy.types.keys import PublicKey
from base64 import b64decode
from tonpy.types.lite_utils.server_list import servers
from tonpy.types.blockid import BlockId, BlockIdExt
from tonpy.types.vmdict import VmDict
from time import sleep, time
from uuid import uuid4

from tonpy.utils.chunks import chunks

if TYPE_CHECKING:
    from tonpy.autogen.block import Block, BlockInfo


def base64_to_hex(b):
    return b64decode(b).hex()


class Bits256:
    def to_hex(self) -> str:
        pass


class MasterchainInfoExt:
    __slots__ = ['mode', 'version', 'capabilities', 'last_utime', 'now', 'state_root_hash', 'last']

    mode: int
    version: int
    capabilities: int
    last_utime: int
    now: int
    state_root_hash: str  # hex
    last: BlockIdExt

    def __init__(self, m):
        self.mode = m.mode
        self.version = m.version
        self.capabilities = m.capabilities
        self.last_utime = m.last_utime
        self.now = m.now
        self.state_root_hash = m.state_root_hash
        self.last = BlockIdExt(blockidext=m.last)


class AccountStateInfo:
    __slots__ = ['root', 'true_root', 'last_trans_lt', 'last_trans_hash', 'gen_lt', 'gen_utime']

    root: Cell
    true_root: Cell
    last_trans_lt: int
    last_trans_hash: str  # hex
    gen_lt: int
    gen_utime: int

    def __init__(self, ac):
        self.root = Cell(ac.root)
        self.true_root = Cell(ac.true_root)
        self.last_trans_lt = ac.last_trans_lt
        self.last_trans_hash = ac.last_trans_hash
        self.gen_lt = ac.gen_lt
        self.gen_utime = ac.gen_utime


class BlockHdrInfo:
    __slots__ = ['blk_id', 'proof', 'virt_blk_root', 'mode']

    blk_id: BlockIdExt
    proof: Cell
    virt_blk_root: Cell
    mode: int

    def __init__(self, blk):
        self.blk_id = BlockIdExt(blockidext=blk.blk_id)
        self.proof = Cell(blk.proof)
        self.virt_blk_root = Cell(blk.virt_blk_root)
        self.mode = blk.mode


class TransactionsInfo:
    blkid: BlockIdExt
    now: int
    prev_trans_lt: int
    prev_trans_hash: str
    transaction: Cell

    def __init__(self, t):
        self.blkid = BlockIdExt(blockidext=t.blkid)
        self.now = t.now
        self.prev_trans_lt = t.prev_trans_lt
        self.prev_trans_hash = t.prev_trans_hash
        self.transaction = Cell(t.transaction)


class TransactionsListInfo:
    lt: int
    hash: str  # hex
    transactions: List[TransactionsInfo]

    def __init__(self, tl):
        self.lt = tl.lt
        self.hash = tl.hash
        self.transactions = list(map(TransactionsInfo, tl.transactions))


class BlockTransactionsListExt:
    incomplete: bool
    req_count: int
    id: BlockIdExt
    transactions: List[Cell]

    def __init__(self, tl):
        self.incomplete = tl.incomplete
        self.req_count = tl.req_count
        self.id = BlockIdExt(blockidext=tl.id)
        self.transactions = list(map(Cell, tl.transactions))


def get_block_info(virt_blk_root) -> "BlockInfo":
    from tonpy.autogen.block import Block, BlockInfo

    block = Block()
    block = block.cell_unpack(virt_blk_root)

    block_info = BlockInfo()
    return block_info.cell_unpack(block.info, True)


class RRLiteClient:
    def __init__(self, servers: list,
                 timeout: int = 1,
                 num_try: int = 5,
                 threads: int = 1,
                 loglevel: int = 0,
                 logprefix: str = ''):
        random.shuffle(servers)
        self.servers = servers

        # for s in servers:
        #     if self.check_server(s):
        #         self.servers.append(s)
        # print(len(self.servers), len(servers))
        # print(servers)

        self.current = -1
        self.client: Optional[LiteClient] = None
        self.timeout = timeout
        self.num_try = num_try
        self.threads = threads
        self.loglevel = loglevel
        self.logprefix = logprefix
        self.rotate()

    def check_server(self, server):
        host = server['ip']
        port = server['port']
        pubkey_base64 = server['id']['key']

        if isinstance(host, int):
            host = ipv4_int_to_str(host)

        pubkey = PublicKey(base64_to_hex(pubkey_base64))

        client = PyLiteClient(
            host=host,
            port=port,
            public_key=pubkey.key,
            timeout=0.6,
            threads=self.threads
        )

        try:
            client.get_time()
            client.stop()
            return True
        except Exception as e:
            return False

    def rotate(self):
        if self.loglevel > 2:
            logger.debug(f"[{self.logprefix}] Call rotate")

        self.current += 1
        if self.current > len(self.servers) - 1:
            self.current = 0

        server = self.servers[self.current]

        if self.loglevel > 200:
            logger.debug(f"[{self.logprefix}] New server: {server['ip']}:{server['port']}")

        host = server['ip']
        port = server['port']

        pubkey_base64 = server['id']['key']
        timeout = self.timeout

        if isinstance(host, int):
            host = ipv4_int_to_str(host)

        pubkey = PublicKey(base64_to_hex(pubkey_base64))

        if self.client is not None:
            if self.loglevel > 2:
                logger.debug(f"[{self.logprefix}] Stop prev client")

            self.client.stop()

        self.client = PyLiteClient(
            host=host,
            port=port,
            public_key=pubkey.key,
            timeout=timeout,
            threads=self.threads
        )

        if self.loglevel > 128:
            logger.debug(f"[{self.logprefix}] End rotate")

    def stop(self):
        self.client.stop()

    def __del__(self):
        self.client.stop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.stop()

    def __getattr__(self, name):
        func = name

        def f(*args, **kwargs):
            try_count = self.num_try

            while True:
                try:
                    start = None
                    uid = None

                    if self.loglevel > 128:
                        start = time()
                        uid = str(uuid4())
                        logger.info(f"[{self.logprefix}] Run request {func} / {uid} with: {args}, {kwargs}")

                    answer = getattr(self.client, func)(*args, **kwargs)

                    if self.loglevel > 128:
                        end = time() - start
                        logger.info(f"[{self.logprefix}] End request {uid} at {end}")

                    return answer
                except Exception as e:
                    if self.loglevel > 0:
                        logger.error(f"[{self.logprefix}] Error: {e}, {traceback.format_exc()}")

                    try_count -= 1
                    if try_count == 0:
                        raise e

                    self.rotate()

        return f


class LiteClient:
    def __init__(self, host: Union[str, int] = None,
                 port: int = None,
                 pubkey: PublicKey = None,
                 pubkey_hex: str = None,
                 pubkey_base64: str = None,
                 timeout: float = 1,
                 threads: int = 1,
                 mode: str = 'ordinary',
                 my_rr_servers: list = None,
                 num_try: int = 5,
                 loglevel: int = 0,
                 logprefix: str = ''):
        """

        :param host:
        :param port:
        :param pubkey:
        :param pubkey_hex:
        :param pubkey_base64:
        :param threads:
        :param timeout:
        :param mode:
            - ordinary
            - roundrobin
        """

        self.loglevel = loglevel
        self.logprefix = logprefix

        if mode == 'ordinary':
            if isinstance(host, int):
                host = ipv4_int_to_str(host)

            if pubkey is None:
                if pubkey_hex is None:
                    if pubkey_base64 is None:
                        raise ValueError(f"[{self.logprefix}] Pass pubkey in any format")
                    else:
                        pubkey = PublicKey(base64_to_hex(pubkey_base64))
                else:
                    pubkey = PublicKey(pubkey_hex)

            self.client = PyLiteClient(
                host=host,
                port=port,
                public_key=pubkey.key,
                timeout=timeout,
                threads=threads
            )
        elif mode == 'roundrobin':
            self.client = RRLiteClient(servers=servers if my_rr_servers is None else my_rr_servers,
                                       timeout=timeout, num_try=num_try, loglevel=loglevel, logprefix=logprefix)
        else:
            raise ValueError(f"[{self.logprefix}] {mode} is not supported")

    def get_connected(self) -> bool:
        return self.client.get_connected()

    def get_time(self) -> int:
        return self.client.get_time()

    def send_message(self, cell):
        """

        :param cell:
        :return:
        """
        return self.client.send_message(cell.cell)

    def get_masterchain_info_ext(self) -> MasterchainInfoExt:
        return MasterchainInfoExt(self.client.get_MasterchainInfoExt())

    def wait_masterchain_seqno(self, seqno, timeout) -> MasterchainInfoExt:
        return MasterchainInfoExt(self.client.wait_masterchain_seqno(seqno, timeout))

    def get_account_state(self, account: Union[str, Address], block: BlockIdExt) -> AccountStateInfo:
        """
        If you trust BlockIdExt hashes - you trust result

        :param account:
        :param block:
        :return:
        """

        if isinstance(account, str):
            account = Address(account)

        return AccountStateInfo(
            self.client.get_AccountState(account.wc, str(int(account.address, 16)), block.blockidext))

    def lookup_block(self, block: BlockId = None,
                     workchain: int = 0,
                     shard: Union[int, str] = 0,
                     seqno: int = 0,
                     lt: int = 0,
                     gen_utime: int = 0) -> BlockHdrInfo:
        """
        WARNING: do not trust result if not yours lite-server

        :param block:
        :param workchain:
        :param shard:
        :param seqno:
        :param lt:
        :param gen_utime:
        :return:
        """

        if block is None:
            if isinstance(shard, str):
                shard = int(shard, 16)

            block = BlockId(workchain, shard, seqno)

        mode = 0
        if block.seqno:
            mode += 1
        if lt:
            mode += 2
        if gen_utime:
            mode += 3

        return BlockHdrInfo(self.client.lookupBlock(mode, block.blockid, lt, gen_utime))

    def get_block_header(self, block: BlockIdExt) -> BlockHdrInfo:
        """The different between lookup_block is in EXACT hash check of BlockIdExt

        :param block:
        :return:
        """

        return BlockHdrInfo(self.client.get_BlockHeader(block.blockidext, 0))

    def get_transactions(self, account: Union[str, Address], from_lt: int, from_hash: str,
                         count: int) -> TransactionsListInfo:
        """Transaction verified by hashes, if you trust from_hash - you trust result
        (except blocks, they have no proof that transaction actually in that block)

        :param account:
        :param from_lt:
        :param from_hash:
        :param count:
        :return:
        """

        if isinstance(account, str):
            account = Address(account)

        return TransactionsListInfo(
            self.client.get_Transactions(count, account.wc, str(int(account.address, 16)), from_lt,
                                         str(int(from_hash, 16))))

    def get_config_all(self, blkid: BlockIdExt, from_not_trusted_keyblock=False) -> Tuple[BlockIdExt, VmDict]:
        """
        By default if you trust BlockIdExt => you trust result, but if `from_not_trusted_keyblock` result will be
        not for requested block, but for keyblock (no proof check there)

        :param blkid:
        :param from_not_trusted_keyblock:
        :return:
        """
        mode = 0
        if from_not_trusted_keyblock:
            mode += 0x8000

        blkid, cell = self.client.get_ConfigAll(mode, blkid.blockidext, not from_not_trusted_keyblock)
        return BlockIdExt(blockidext=blkid), VmDict(32, False, Cell(cell))

    def get_block(self, blkid: BlockIdExt) -> Cell:
        """
        If you trust BlockIdExt - you trust result

        :param blkid:
        :return:
        """

        return Cell(self.client.get_Block(blkid.blockidext))

    def get_libraries(self, libs_hashes: Union[List[int], List[str]]) -> VmDict:
        """
        Return dict with libs, if you trust hashes - you trust result

        :param libs_hashes:
        :return:
        """

        if isinstance(libs_hashes[0], int):
            libs_hashes = list(map(str, libs_hashes))
        else:
            libs_hashes = list(map(lambda x: str(int(x, 16)), libs_hashes))

        if len(libs_hashes) > 16:
            libs_hashes = list(chunks(libs_hashes, 16))
        else:
            libs_hashes = [libs_hashes]

        answer = VmDict(key_len=256, py_dict=self.client.get_Libraries(libs_hashes[0]))

        if len(libs_hashes) > 1:
            for tmp in libs_hashes[1:]:
                tmp_answer = VmDict(key_len=256, py_dict=self.client.get_Libraries(tmp))
                answer.combine_with(tmp_answer)

        return answer

    def get_one_transaction(self, blkid: BlockIdExt, account_address: Union[Address, str] = None,
                            lt: int = None) -> Cell:
        """Will check proof, if you trust blkid - you trust result"""

        if isinstance(account_address, str):
            account_address = Address(account_address)

        return Cell(
            self.client.get_OneTransaction(blkid.blockidext, account_address.wc, str(int(account_address.address, 16)),
                                           lt))

    def list_block_transactions_ext(self, blkid: BlockIdExt,
                                    count: int,
                                    account_address: Union[Union[Address, int], str] = None,
                                    lt: int = None,
                                    check_proof: bool = False,
                                    reverse_mode: bool = False):
        mode = 0

        if check_proof:
            mode += 32

        if reverse_mode:
            mode += 64

        if account_address is not None or lt is not None:
            if account_address is not None and lt is not None:
                mode += 128
            else:
                raise ValueError("Not valid params, pass account_address and lt")

        if isinstance(account_address, Address):
            account_address = account_address.address

        if isinstance(account_address, str):
            account_address = int(account_address, 16)

        if isinstance(account_address, int):
            account_address = str(account_address)

        return BlockTransactionsListExt(
            self.client.get_listBlockTransactionsExt(blkid.blockidext, mode, count, account_address, lt))

    def get_all_shards_info(self, blkid: BlockIdExt) -> List[BlockId]:
        data = self.client.get_AllShardsInfo(blkid.blockidext)
        return list(map(lambda x: BlockId(blockid=x), data))

    def admin_add_user(self, pubkey: Union[str, int], valid_until: int, ratelimit: int) -> str:
        if isinstance(pubkey, str):
            pubkey = str(int(pubkey, 16))
        else:
            pubkey = str(pubkey)

        return self.client.admin_AddUser(pubkey, valid_until, ratelimit)

    def admin_get_stats(self):
        return self.client.admin_getStatData()

    def wait_connected(self, timeout: int):
        """Wait until connected with timeout, throw error if not connected"""
        return self.client.wait_connected(datetime.datetime.now().timestamp() + timeout)

    @staticmethod
    def get_one(timeout: int = 1, threads: int = 1) -> "LiteClient":
        server = random.choice(servers)

        return LiteClient(host=server['ip'],
                          port=server['port'],
                          pubkey_base64=server['id']['key'],
                          timeout=timeout,
                          threads=threads)

    def __del__(self):
        self.client.stop()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.stop()
