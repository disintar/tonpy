from ctypes import c_void_p, CDLL, c_char_p, c_int, c_bool, c_uint, c_ulonglong
from typing import Union
import json

from tonpy.types import Cell, CellSlice, VmDict, StackEntry


class EmulatorExtern:
    """This is needed to check new versions of TON, please use native python bindings instead"""

    def __init__(self, cdll_path: str, config: Union[VmDict, Union[Cell, str]], tvm_verbosity: int = 0):
        self.cdll_path = cdll_path
        self.libemulator = libemulator = CDLL(self.cdll_path)
        self.vm_log = None

        emulator_set_verbosity_level = libemulator.emulator_set_verbosity_level
        emulator_set_verbosity_level.restype = c_bool
        emulator_set_verbosity_level.argtypes = [c_int]
        emulator_set_verbosity_level(1)

        transaction_emulator_create = libemulator.transaction_emulator_create
        transaction_emulator_create.restype = c_void_p
        transaction_emulator_create.argtypes = [c_char_p, c_int]

        if isinstance(config, VmDict):
            config = config.get_cell()

        if isinstance(config, Cell):
            config = config.to_boc()

        self.emulator = transaction_emulator_create(config.encode(), 1)

        self.transaction = None
        self.account = None

    def set_rand_seed(self, rand_seed: Union[str, int]) -> bool:
        if isinstance(rand_seed, int):
            rand_seed = hex(rand_seed).upper()[2:]

        transaction_emulator_set_rand_seed = self.libemulator.transaction_emulator_set_rand_seed
        transaction_emulator_set_rand_seed.restype = c_bool
        transaction_emulator_set_rand_seed.argtypes = [c_void_p, c_char_p]

        return transaction_emulator_set_rand_seed(self.emulator, rand_seed.zfill(64).encode())

    def set_prev_blocks_info(self, prev_blocks: list) -> bool:
        transaction_emulator_set_prev_blocks_info = self.libemulator.transaction_emulator_set_prev_blocks_info
        transaction_emulator_set_prev_blocks_info.restype = c_bool
        transaction_emulator_set_prev_blocks_info.argtypes = [c_void_p, c_char_p]

        return transaction_emulator_set_prev_blocks_info(self.emulator,
                                                         StackEntry(prev_blocks).serialize().to_boc().encode())

    def set_libs(self, libs_data: Union[VmDict, Cell]) -> bool:
        if isinstance(libs_data, VmDict):
            libs_data = libs_data.get_cell()

        transaction_emulator_set_libs = self.libemulator.transaction_emulator_set_libs
        transaction_emulator_set_libs.restype = c_bool
        transaction_emulator_set_libs.argtypes = [c_void_p, c_char_p]

        return transaction_emulator_set_libs(self.emulator, libs_data.to_boc().encode())

    def set_unixtime(self, time: int) -> bool:
        transaction_emulator_set_unixtime = self.libemulator.transaction_emulator_set_unixtime
        transaction_emulator_set_unixtime.restype = c_bool
        transaction_emulator_set_unixtime.argtypes = [c_void_p, c_uint]

        return transaction_emulator_set_unixtime(self.emulator, time)

    def set_lt(self, lt: int) -> bool:
        transaction_emulator_set_lt = self.libemulator.transaction_emulator_set_lt
        transaction_emulator_set_lt.restype = c_bool
        transaction_emulator_set_lt.argtypes = [c_void_p, c_ulonglong]

        return transaction_emulator_set_lt(self.emulator, lt)

    def raw_emulate_transaction(self, account_state: Union[Cell, str], in_msg: Union[Cell, str]) -> dict:
        if isinstance(account_state, Cell):
            account_state = account_state.to_boc()

        if isinstance(in_msg, Cell):
            in_msg = in_msg.to_boc()

        transaction_emulator_emulate_transaction = self.libemulator.transaction_emulator_emulate_transaction
        transaction_emulator_emulate_transaction.restype = c_char_p
        transaction_emulator_emulate_transaction.argtypes = [c_void_p, c_char_p, c_char_p]

        return json.loads(transaction_emulator_emulate_transaction(self.emulator,
                                                                   account_state.encode(),
                                                                   in_msg.encode()).decode())

    def raw_emulate_tick_tock_transaction(self, account_state: Union[Cell, str], is_tock: bool) -> dict:
        if isinstance(account_state, Cell):
            account_state = account_state.to_boc()

        transaction_emulator_emulate_tick_tock_transaction = self.libemulator.transaction_emulator_emulate_tick_tock_transaction
        transaction_emulator_emulate_tick_tock_transaction.restype = c_char_p
        transaction_emulator_emulate_tick_tock_transaction.argtypes = [c_void_p, c_char_p, c_bool]
        return json.loads(
            transaction_emulator_emulate_tick_tock_transaction(self.emulator, account_state.encode(), is_tock).decode())

    def emulate_tick_tock_transaction(self, account_state: Union[Cell, str], is_tock: bool, unixtime: int, lt: int):
        self.set_unixtime(unixtime)
        self.set_lt(lt)

        data = self.raw_emulate_tick_tock_transaction(account_state, is_tock)
        success = data['success']

        if success:
            self.transaction = CellSlice(data['transaction'])
            self.account = CellSlice(data['shard_account'])
            if data['actions']:
                self.action = CellSlice(data['actions'])

        return success

    def emulate_transaction(self, account_state: Union[Cell, str], in_msg: Union[Cell, str], unixtime: int, lt: int):
        self.set_unixtime(unixtime)
        self.set_lt(lt)

        data = self.raw_emulate_transaction(account_state, in_msg)
        success = data['success']

        if success:
            self.vm_log = data['vm_log']
            self.transaction = CellSlice(data['transaction'])
            self.account = CellSlice(data['shard_account'])
            if data['actions']:
                self.action = CellSlice(data['actions'])

        return success

    def __del__(self):
        transaction_emulator_destroy = self.libemulator.emulator_set_verbosity_level
        transaction_emulator_destroy.restype = None
        transaction_emulator_destroy.argtypes = [c_void_p]
        transaction_emulator_destroy(self.emulator)
