from typing import Union, List

from tonpy.types.cell import Cell
from tonpy.types.cellslice import CellSlice
from tonpy.types.cellbuilder import begin_cell
from tonpy.types.address import Address
from datetime import datetime
from tonpy.types.blockid import BlockIdExt
from tonpy.types.stack import Stack


class C7:
    def __init__(self, magic: int = 0x076ef1ea, actions: int = 0, msgs_sent: int = 0,
                 time: Union[int, datetime] = None, block_lt: int = 0, trans_lt: int = 0,
                 rand_seed: Union[int, str] = None, balance_grams: int = 0, balance_extra: Cell = None,
                 address: Union[Union[dict, Cell], Address] = None, global_config: Cell = None, my_code: Cell = None,
                 storage_fees: int = 0, income_grams: int = 0, income_extra: Cell = None,
                 last_mc_blocks: Union[List[BlockIdExt], List[List]] = None,
                 prev_key_block: Union[BlockIdExt, List] = None, due_payment: int = 0):

        if last_mc_blocks is None:
            self.last_mc_blocks = []
        else:
            self.last_mc_blocks = last_mc_blocks

            if len(self.last_mc_blocks) > 0 and isinstance(self.last_mc_blocks[0], BlockIdExt):
                self.last_mc_blocks = [i.to_data() for i in self.last_mc_blocks]

        self.prev_key_block = prev_key_block

        if isinstance(self.prev_key_block, BlockIdExt):
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
        elif isinstance(address, Address):
            self.address = begin_cell().store_address(address).end_cell().begin_parse()
        else:
            self.address = begin_cell().store_address(
                f"{address['workchain']}:{address['address']}").end_cell().begin_parse()

        self.global_config = global_config
        self.my_code = my_code
        self.income_grams = income_grams
        self.income_extra = income_extra
        self.storage_fees = storage_fees
        self.due_payment = due_payment

    def to_data(self):
        return [
            self.magic,                           # [0] magic: 0x076ef1ea
            self.actions,                         # [1] actions: Integer
            self.msgs_sent,                       # [2] msgs_sent: Integer
            self.time,                            # [3] unixtime: Integer
            self.block_lt,                        # [4] block_lt: Integer
            self.trans_lt,                        # [5] trans_lt: Integer
            self.rand_seed,                       # [6] rand_seed: Integer
            [self.balance_grams, self.balance_extra],  # [7] balance_remaining: [Integer (Maybe Cell)]
            self.address,                         # [8] myself: MsgAddressInt
            self.global_config,                   # [9] global_config: (Maybe Cell)
            self.my_code,                         # [10] my_code
            [self.income_grams, self.income_extra],    # [11] income_remaining: [Integer (Maybe Cell)]
            self.storage_fees,                    # [12] storage_fees
            self.last_mc_blocks,                  # [13] last_mc_blocks
            self.prev_key_block,                  # [14] prev_key_block
            0,                                    # [15] unpacked_config_tuple (computed in C++ with config)
            self.due_payment,                     # [16] due_payment
            0                                     # [17] precompiled_gas_usage (computed in C++ with config)
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
