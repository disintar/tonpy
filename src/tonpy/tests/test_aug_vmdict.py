from pathlib import Path
import sys
from random import random
from time import time

import pytest

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.vmdict import VmDict
from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell
from tonpy.libs.python_ton import PyAugmentationCheckData, PyCellSlice
from tonpy.types import CellBuilder, CellSlice
from typing import Optional

from tonpy.types.vmdict import AugmentedData


class BasicAug(AugmentedData):
    def eval_leaf(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        cs = CellBuilder().store_uint(1, 64).begin_parse()
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
    print(d[0], d[1])


if __name__ == "__main__":
    test_set_get_item()
