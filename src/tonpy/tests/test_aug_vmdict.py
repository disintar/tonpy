from pathlib import Path
import sys
from random import random
from time import time

import pytest

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.vmdict import VmDict, TypedVmDict
from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell
from tonpy.libs.python_ton import PyAugmentationCheckData, PyCellSlice
from tonpy.types import CellBuilder, CellSlice
from typing import Optional

from tonpy.types.vmdict import AugmentedData


# Example of augment usage
class BasicAug(AugmentedData):
    def eval_leaf(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        # on leaf creation automatically extract needed data and store as extra
        value = cs.load_uint(32) + 10
        cs = CellBuilder().store_uint(value, 64).begin_parse()
        return True, cs

    def skip_extra(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        cs.skip_bits(64)
        return True, cs

    def eval_fork(self, left: CellSlice, right: CellSlice) -> (bool, Optional[CellSlice]):
        a = left.load_uint(64)
        b = right.load_uint(64)
        return True, CellBuilder().store_uint(a + b, 64).begin_parse()

    def eval_empty(self) -> (bool, Optional[CellSlice]):
        cs = CellBuilder().store_uint(0, 64).begin_parse()
        return True, cs


def test_set_get_item():
    d = VmDict(256, aug=BasicAug())
    d[0] = CellBuilder().store_uint(0, 32).end_cell().begin_parse()
    d[1] = CellBuilder().store_uint(1, 32).end_cell().begin_parse()

    v1 = d[0]
    assert v1.data.load_uint(32) == 0
    assert v1.extra.load_uint(64) == 10

    v2 = d[1]
    assert v2.data.load_uint(32) == 1
    assert v2.extra.load_uint(64) == 11


def test_config():
    from tonpy.utils.global_config import CFG_TEST
    from tonpy.autogen.block import ConfigParam

    config_data = VmDict(32, False, CFG_TEST)

    for i in config_data:
        print(i)

    # _ config_addr:bits256 = ConfigParam 0;
    config_addr = hex(int(ConfigParam(0).fetch(config_data[0].load_ref()).config_addr, 2))[2:].upper()
    assert config_addr == '5555555555555555555555555555555555555555555555555555555555555555'

    # _ elector_addr:bits256 = ConfigParam 1;
    elector_addr = hex(int(ConfigParam(1).fetch(config_data[1].load_ref()).elector_addr, 2))[2:].upper()
    assert elector_addr == '3333333333333333333333333333333333333333333333333333333333333333'

    # _ minter_addr:bits256 = ConfigParam 2;
    minter_addr = hex(int(ConfigParam(2).fetch(config_data[2].load_ref()).minter_addr, 2))[2:].upper()
    assert minter_addr == '0'

    # _ dns_root_addr:bits256 = ConfigParam 4;
    dns_root_addr = hex(int(ConfigParam(4).fetch(config_data[4].load_ref()).dns_root_addr, 2))[2:].upper()
    assert dns_root_addr == 'E56754F83426F69B09267BD876AC97C44821345B7E266BD956A7BFBFB98DF35C'

    # burning_config#01
    #   blackhole_addr:(Maybe bits256)
    #   fee_burn_num:# fee_burn_denom:# { fee_burn_num <= fee_burn_denom } { fee_burn_denom >= 1 } = BurningConfig;
    # _ BurningConfig = ConfigParam 5;
    burning_config = ConfigParam(5).fetch(config_data[5].load_ref()).x
    assert burning_config.fee_burn_denom == 2
    assert burning_config.fee_burn_num == 1
    assert hex(int(burning_config.blackhole_addr.value, 2))[2:].upper() \
           == 'FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF'

