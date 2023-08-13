from tonpy.libs.python_ton import PyEmulator
from tonpy.types import VmDict, Cell
from typing import Union


class Emulator:
    def __init__(self, config: Union[Cell, VmDict]):
        self.emulator: PyEmulator = PyEmulator(config.get_cell().cell)

    def emulate_transaction(self, shard_account: Cell, message: Cell, unixtime: int, lt: int) -> bool:
        return self.emulator.emulate_transaction(shard_account.cell, message.cell, str(unixtime), str(lt),
                                                 1 if lt >= 3709412000000 else 0)

    def emulate_tick_tock_transaction(self, shard_account: Cell, is_tock: bool, unixtime: int, lt: int) -> bool:
        return self.emulator.emulate_tick_tock_transaction(shard_account.cell, is_tock, str(unixtime), str(lt),
                                                           1 if lt >= 3709412000000 else 0)

    def set_rand_seed(self, seed: Union[int, hex]) -> None:
        if isinstance(seed, int):
            seed = hex(seed)[2:].upper()

        self.emulator.set_rand_seed(seed)

    def set_ignore_chksig(self, flag: bool) -> None:
        self.emulator.set_ignore_chksig(flag)

    def set_libs(self, libs: VmDict) -> None:
        self.emulator.set_libs(libs.get_cell())

    def set_debug_enabled(self, flag: bool) -> None:
        self.emulator.set_debug_enabled(flag)

    @property
    def elapsed_time(self):
        return self.emulator.elapsed_time

    @property
    def transaction(self):
        return Cell(self.emulator.transaction_cell).begin_parse()

    @property
    def account(self):
        return Cell(self.emulator.account_cell).begin_parse()

    @property
    def actions(self):
        return Cell(self.emulator.actions_cell).begin_parse()
