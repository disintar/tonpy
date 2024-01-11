from typing import Union, List
from tonpy.types import Cell, CellSlice, Stack, begin_cell
from datetime import datetime


class BlockId:
    def __init__(self, wc: int = 0,
                 seqno: int = 0,
                 shard: Union[str, int] = 0,
                 root_hash: Union[str, int] = 0,
                 file_hash: Union[str, int] = 0):
        self.wc = wc
        self.shard = int(shard, 16) if isinstance(shard, str) else shard
        self.seqno = seqno
        self.root_hash = int(root_hash, 16) if isinstance(root_hash, str) else root_hash
        self.file_hash = int(file_hash, 16) if isinstance(file_hash, str) else file_hash

    def to_data(self):
        # [ wc:Integer shard:Integer seqno:Integer root_hash:Integer file_hash:Integer ] = BlockId;
        return [self.wc, self.shard, self.seqno, self.root_hash, self.file_hash]


class C7:
    def __init__(self, magic: int = 0x076ef1ea, actions: int = 0, msgs_sent: int = 0,
                 time: Union[int, datetime] = None, block_lt: int = 0, trans_lt: int = 0,
                 rand_seed: Union[int, str] = None, balance_grams: int = 0, balance_extra: Cell = None,
                 address: Union[dict, Cell] = None, global_config: Cell = None, my_code: Cell = None,
                 storage_fees: int = 0, income_grams: int = 0, income_extra: Cell = None,
                 last_mc_blocks: Union[List[BlockId], List[List]] = None, prev_key_block: Union[BlockId, List] = None):

        if last_mc_blocks is None:
            self.last_mc_blocks = []
        else:
            self.last_mc_blocks = last_mc_blocks

            if len(self.last_mc_blocks) > 0 and isinstance(self.last_mc_blocks[0], BlockId):
                self.last_mc_blocks = [i.to_data() for i in self.last_mc_blocks]

        self.prev_key_block = prev_key_block

        if isinstance(self.prev_key_block, BlockId):
            self.prev_key_block = self.prev_key_block.to_data()

        self.magic = magic
        self.actions = actions
        self.msgs_sent = msgs_sent

        if time is None:
            time = datetime.now()

        if isinstance(time, datetime):
            self.time = int(time.timestamp())
        else:
            self.time = time

        self.block_lt = block_lt
        self.trans_lt = trans_lt

        if isinstance(rand_seed, str):
            self.rand_seed = int(rand_seed, 16)
        else:
            self.rand_seed = rand_seed

        self.balance_grams = balance_grams
        self.balance_extra = balance_extra if balance_extra is not None else begin_cell().end_cell()

        if isinstance(address, CellSlice):
            self.address = address
        elif address is None:
            self.address = begin_cell().end_cell().begin_parse()
        else:
            self.address = begin_cell().store_address(
                f"{address['workchain']}:{address['address']}").end_cell().begin_parse()

        self.global_config = global_config
        self.my_code = my_code
        self.income_grams = income_grams
        self.income_extra = income_extra
        self.storage_fees = storage_fees

    def to_data(self):
        return [
            self.magic,  # [ magic:0x076ef1ea
            self.actions,  # actions:Integer
            self.msgs_sent,  # msgs_sent:Integer
            self.time,  # unixtime:Integer
            self.block_lt,  # block_lt:Integer
            self.trans_lt,  # trans_lt:Integer
            self.rand_seed,  # rand_seed:Integer
            [self.balance_grams, self.balance_extra],  # balance_remaining:[Integer (Maybe Cell)]
            self.address,  # myself:MsgAddressInt
            self.global_config,  # global_config:(Maybe Cell)
            self.my_code,
            [self.income_grams, self.income_extra],
            self.storage_fees,
            self.last_mc_blocks,
            self.prev_key_block
        ]


class StepInfo:
    stack: Stack = None
    gas_consumed: int = None
    gas_remaining: int = None
    next_op: str = None

    def __init__(self, stack_info):
        self.stack = Stack(prev_stack=stack_info.stack)
        self.gas_consumed = int(stack_info.gas_consumed)
        self.gas_remaining = int(stack_info.gas_remaining)
        self.next_op = None