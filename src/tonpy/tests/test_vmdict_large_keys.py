# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys
from random import random
from time import time

import pytest

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.vmdict import VmDict
from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell
from tonpy.data_for_tests.dict_test_boc import config_44, reveal_dict_boc


def test_set_get_keycs_direct():
    d = VmDict(264)

    v1 = CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse()
    d.set_keycs(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(), v1)

    v2 = CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell()
    d.set_ref_keycs(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(), v2)

    d.set_builder_keycs(CellBuilder().store_uint(2, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(),
                        CellBuilder().store_uint(0, 8))

    value = d.lookup_keycs(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v1.get_hash()

    value = d.lookup_delete_keycs(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v1.get_hash()

    try:
        d.lookup_keycs(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
        assert False
    except RuntimeError:
        pass

    value = d.lookup_ref_keycs(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v2.get_hash()

    value = d.lookup_delete_ref_keycs(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v2.get_hash()

    try:
        value = d.lookup_ref_keycs(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
        assert False
    except RuntimeError:
        pass


def test_set_get_keycs_direct():
    d = VmDict(264)

    v1 = CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse()
    d.set(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(), v1)

    v2 = CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell()
    d.set_ref(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(), v2)

    d.set_builder(CellBuilder().store_uint(2, 8).store_uint(2 ** 254, 256).end_cell().begin_parse(),
                        CellBuilder().store_uint(0, 8))

    value = d.lookup(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v1.get_hash()

    value = d.lookup_delete(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v1.get_hash()

    try:
        d.lookup(CellBuilder().store_uint(0, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
        assert False
    except RuntimeError:
        pass

    value = d.lookup_ref(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v2.get_hash()

    value = d.lookup_delete_ref(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
    assert value.get_hash() == v2.get_hash()

    try:
        value = d.lookup_ref(CellBuilder().store_uint(1, 8).store_uint(2 ** 254, 256).end_cell().begin_parse())
        assert False
    except RuntimeError:
        pass
