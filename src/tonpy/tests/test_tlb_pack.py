import pytest

from tonpy.tlb_gen.py import add_tlb, parse_tlb
from enum import Enum
import bitstring
from bitstring import BitArray
from tonpy.types import TLB, TLBComplex, Cell, CellSlice, CellBuilder, RecordBase
from typing import Optional, Union
from itertools import product


def test_nat_unpack():
    # language=tl-b
    tlb_text = """
    a$10001 a:# b:(#< 10) c:(#<= 64) d:(## 64) = A;
    b$10000 = A;
    """

    # Pack A.a
    test_a = CellBuilder() \
        .store_bitstring('10001') \
        .store_uint(int('1' * 32, 2), 32) \
        .store_uint_less(10, 9) \
        .store_uint_leq(64, 64) \
        .store_uint(int('1' * 64, 2), 64)

    test_a_cs = test_a.begin_parse()
    test_a_c = test_a.end_cell()

    # Pack A.b
    test_b = CellBuilder().store_bitstring('10000')

    test_b_cs = test_b.begin_parse()
    test_b_c = test_b.end_cell()

    add_tlb(tlb_text, globals())

    rec_a = A.Record_a()
    assert rec_a.a is None
    assert rec_a.b is None
    assert rec_a.c is None
    assert rec_a.d is None

    assert rec_a.unpack(test_a_cs) is True

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)

    rec_a = A.Record_a()

    assert rec_a.a is None
    assert rec_a.b is None
    assert rec_a.c is None
    assert rec_a.d is None

    assert rec_a.cell_unpack(test_a_c) is True

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)

    rec_b = A.Record_b()
    assert rec_b.unpack(test_b_cs) is True
    assert rec_b.cell_unpack(test_b_c) is True


def test_complex_unpack():
    # language=tl-b
    tlb_text = """
    a$10001 a:# b:(#< 10) c:(#<= 64) d:(## 64) = A;
    b$10000 = A;
    """

    # Pack A.a
    test_a = CellBuilder() \
        .store_bitstring('10001') \
        .store_uint(int('1' * 32, 2), 32) \
        .store_uint_less(10, 9) \
        .store_uint_leq(64, 64) \
        .store_uint(int('1' * 64, 2), 64)

    test_a_cs = test_a.begin_parse()
    test_a_c = test_a.end_cell()

    # Pack A.b
    test_b = CellBuilder().store_bitstring('10000')

    test_b_cs = test_b.begin_parse()
    test_b_c = test_b.end_cell()

    add_tlb(tlb_text, globals())

    tA = A()
    tc = tA.cell_unpack(test_b_c)
    tcs = tA.unpack(test_b_cs)

    assert type(tc) is A.Record_b
    assert tc.get_tag_enum() == A.Tag.b
    assert tc.get_tag() == 16
    assert tc.get_tag_len() == 5
    assert type(tcs) is A.Record_b
    assert tcs.get_tag_enum() == A.Tag.b
    assert tcs.get_tag() == 16
    assert tcs.get_tag_len() == 5

    tA = A()
    rec_a = tA.cell_unpack(test_a_c)

    assert type(rec_a) is A.Record_a
    assert rec_a.get_tag_enum() == A.Tag.a
    assert rec_a.get_tag() == 17
    assert rec_a.get_tag_len() == 5

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)

    rec_a = tA.unpack(test_a_cs)
    assert rec_a.get_tag_enum() == A.Tag.a
    assert rec_a.get_tag() == 17
    assert rec_a.get_tag_len() == 5

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)
