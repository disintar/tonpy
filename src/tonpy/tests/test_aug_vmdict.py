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
    from tonpy.autogen.block import ConfigParam, WorkchainDescr

    config_data = VmDict(32, False, CFG_TEST)

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


def test_typed_solo():
    from tonpy.autogen.block import ConfigParam, WorkchainDescr

    # check for iterator
    items = list(TypedVmDict(WorkchainDescr(), 32, False,
                             'te6ccuEBAQEAXgC8ALfQUy7nTs8AAAJwACrYn7aHDoYaZOELB7fIx0lsFfzu58bxcmSlH++c6KojdwX2/yWZOw/Zr08OxAx1OQZWjQc9ppdrOeJEc5dIgaEAAAAAD/////gAAAAAAAAABEhiGEM='))

    assert len(items) == 1
    a = items[0]

    # check for __getitem__
    b = TypedVmDict(WorkchainDescr(), 32, False,
                    'te6ccuEBAQEAXgC8ALfQUy7nTs8AAAJwACrYn7aHDoYaZOELB7fIx0lsFfzu58bxcmSlH++c6KojdwX2/yWZOw/Zr08OxAx1OQZWjQc9ppdrOeJEc5dIgaEAAAAAD/////gAAAAAAAAABEhiGEM=')
    b = [0, b[0]]

    for j in [a, b]:
        assert j[0] == 0

        from tonpy import RecordBase
        assert issubclass(type(j[1]), RecordBase)
        assert j[1].to_dict(rec_unpack=True) == {'enabled_since': 1573821854, 'actual_min_split': 0, 'min_split': 0,
                                                 'max_split': 4, 'basic': True, 'active': True, 'accept_msgs': True,
                                                 'flags': 0,
                                                 'zerostate_root_hash': '0101010110110001001111110110110100001110000111010000110000110100110010011100001000010110000011110110111110010001100011101001001011011000001010111111100111011101110011111000110111100010111001001100100101001010001111111101111100111001110100010101010001000110',
                                                 'zerostate_file_hash': '1110111000001011111011011111111001001011001100100111011000011111101100110101111010011110000111011000100000011000111010100111001000001100101011010001101000001110011110110100110100101110110101100111001111000100100010001110011100101110100100010000001101000010',
                                                 'version': 0, 'format': {'vm_version': -1, 'vm_mode': 0}}


def test_param_20():
    from tonpy.autogen.block import ConfigParam, WorkchainDescr
    a = 'te6ccuEBAQEATACYAJTRAAAAAAAAAGQAAAAAAA9CQN4AAAAAJxAAAAAAAAAAD0JAAAAAAAIWDsAAAAAAAAAnEAAAAAACNJNAAAAAAAX14QAAAAAAO5rKAD0ju+Y='
    c = ConfigParam(20).fetch(Cell(a), rec_unpack=True)
    assert c.to_dict(rec_unpack=True) == {'x': {'flat_gas_limit': 100, 'flat_gas_price': 1000000,
                                                'other': {'gas_price': 655360000, 'gas_limit': 1000000,
                                                          'special_gas_limit': 35000000, 'gas_credit': 10000,
                                                          'block_gas_limit': 37000000, 'freeze_due_limit': 100000000,
                                                          'delete_due_limit': 1000000000}}}
