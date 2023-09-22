from tonpy.libs.python_ton import PyEmulator
from tonpy.types import VmDict, Cell, CellSlice
from typing import Union


class Emulator:
    def __init__(self, config: Union[Cell, VmDict]):
        if isinstance(config, VmDict):
            config = config.get_cell().cell
        else:
            config = config.cell

        self.emulator: PyEmulator = PyEmulator(config)

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
    def elapsed_time(self) -> int:
        return self.emulator.elapsed_time

    @property
    def transaction(self, as_cs=True) -> Union[Cell, CellSlice]:
        c = Cell(self.emulator.transaction_cell)

        if as_cs:
            return c.begin_parse()
        else:
            return c

    @property
    def account(self, as_cs=True) -> Union[Cell, CellSlice]:
        c = Cell(self.emulator.account_cell)

        if as_cs:
            return c.begin_parse()
        else:
            return c

    @property
    def actions(self, as_cs=True) -> Union[Cell, CellSlice]:
        c = Cell(self.emulator.actions_cell)

        if as_cs:
            return c.begin_parse()
        else:
            return c
