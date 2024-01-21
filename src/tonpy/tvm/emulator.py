# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PyEmulator

from tonpy import Stack, StackEntry
from tonpy.types import VmDict, Cell, CellSlice, begin_cell
from tonpy.types.blockid import BlockId
from typing import Union, Tuple, List


class Emulator:
    def __init__(self, config: Union[Cell, VmDict]):
        if isinstance(config, VmDict):
            config = config.get_cell().cell
        else:
            config = config.cell

        self.emulator: PyEmulator = PyEmulator(config)

    def emulate_transaction(self, shard_account: Cell, message: Cell, unixtime: int, lt: int,
                            force_uninit=False) -> bool:
        return self.emulator.emulate_transaction(shard_account.cell, message.cell, str(unixtime), str(lt),
                                                 1 if lt >= 3709412000000 else 0, force_uninit)

    def emulate_tick_tock_transaction(self, shard_account: Cell, is_tock: bool, unixtime: int, lt: int) -> bool:
        return self.emulator.emulate_tick_tock_transaction(shard_account.cell, is_tock, str(unixtime), str(lt),
                                                           1 if lt >= 3709412000000 else 0)

    def set_prev_blocks_info(self, prev_blocks_info: Union[Tuple[List[BlockId], BlockId], Tuple[List, List]]):
        if len(prev_blocks_info) > 0 and len(prev_blocks_info[0]) > 0 and isinstance(prev_blocks_info[0][0], BlockId):
            prev_blocks_info[0] = [i.to_data() for i in prev_blocks_info[0]]

        if isinstance(prev_blocks_info[1], BlockId):
            prev_blocks_info[1] = prev_blocks_info[1].to_data()

        self.emulator.set_prev_blocks_info(StackEntry(value=prev_blocks_info).entry)

    def set_rand_seed(self, seed: Union[int, hex]) -> None:
        if isinstance(seed, int):
            seed = hex(seed)[2:].upper().zfill(64)

        self.emulator.set_rand_seed(seed)

    def set_ignore_chksig(self, flag: bool) -> None:
        self.emulator.set_ignore_chksig(flag)

    def set_libs(self, libs: VmDict) -> None:
        self.emulator.set_libs(libs.get_cell().cell)

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


if __name__ == "__main__":
    cfg = VmDict(32)
    cfg.set_builder(0, begin_cell())

    em = Emulator(cfg)
    em.set_prev_blocks_info([[0], 0])
