# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.libs.python_ton import PyCell, PyCellSlice, PyCellBuilder, PyDict, PyEmulator, parse_string_to_cell, \
    load_as_cell_slice


def test_load_boc():
    cell = parse_string_to_cell('te6ccuEBAQEACgAUABAAAAAAAAAAe4EqE1s=')
    cs = load_as_cell_slice(cell, False)
    assert cell.get_hash() == cs.get_hash()
    assert cs.load_int(64) == '123'
