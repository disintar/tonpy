# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

import pickle as pck
from tonpy.types import Cell, CellSlice, CellBuilder


def test_pck_cell():
    c = Cell("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    dumped_cell = pck.dumps(c)
    loaded_c = pck.loads(dumped_cell)
    assert loaded_c.get_hash() == c.get_hash()
    assert isinstance(loaded_c, Cell)


def test_pck_cell_slice():
    cs = CellSlice("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    dumped_cell = pck.dumps(cs)
    loaded_cs = pck.loads(dumped_cell)
    assert loaded_cs.get_hash() == cs.get_hash()
    assert isinstance(loaded_cs, CellSlice)
    assert loaded_cs.load_uint(32) == cs.load_uint(32)


def test_pck_cell_builder():
    cb = CellBuilder("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    dumped_cell = pck.dumps(cb)
    loaded_cb = pck.loads(dumped_cell)
    assert loaded_cb.get_hash() == cb.get_hash()
    assert isinstance(loaded_cb, CellBuilder)

    cb.store_uint(0, 32)
    loaded_cb.store_uint(0, 32)

    assert cb.bits == loaded_cb.bits
    assert cb.refs == loaded_cb.refs
