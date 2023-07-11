import pytest

from tonpy.tlb_gen.py import add_tlb, parse_tlb
from enum import Enum
import bitstring
from tonpy.types import TLB, TLBComplex, Cell, CellSlice, CellBuilder
from typing import Optional, Union
from itertools import product


def test_tag_multi_bits():
    # language=tl-b
    add_tlb("""
    a$00 = AMultiTagBits;
    b$10 = AMultiTagBits;
    c$01 = AMultiTagBits;
    """, globals())

    a_instance = CellBuilder().store_bitstring("00").begin_parse()
    b_instance = CellBuilder().store_bitstring("10").begin_parse()
    c_instance = CellBuilder().store_bitstring("01").begin_parse()

    A_record = AMultiTagBits()  # noqa
    assert A_record.get_tag(a_instance) == A_record.Tag.a
    assert A_record.get_tag(b_instance) == A_record.Tag.b
    assert A_record.get_tag(c_instance) == A_record.Tag.c


def test_tag_multi_int():
    # language=tl-b
    add_tlb("""
    a#32 = AMultiTagInt;
    b#1111 = AMultiTagInt;
    c#5FE = AMultiTagInt;
    """, globals())

    a_instance = CellBuilder().store_uint(0x32, 8).begin_parse()
    b_instance = CellBuilder().store_uint(0x1111, 16).begin_parse()
    c_instance = CellBuilder().store_uint(0x5fe, 12).begin_parse()

    A_record = AMultiTagInt()  # noqa
    assert A_record.get_tag(a_instance) == A_record.Tag.a
    assert A_record.get_tag(b_instance) == A_record.Tag.b
    assert A_record.get_tag(c_instance) == A_record.Tag.c


def test_tag_multi_int_large():
    tlb_text = ""

    for i in range(64):
        tag = hex(i)[2:].zfill(2)
        tlb_text += f"a{i}#{tag} = ALargeIntTags;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeIntTags()  # noqa

    for i in range(64):
        instance = CellBuilder().store_uint(i, 8).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{i}", globals(), locals())


def test_tag_multi_bits_large():
    tags = [''.join(tag) for tag in list(product('10', repeat=6))]

    tlb_text = ""

    for tag in tags:
        tag_name = int(tag, 2)
        tlb_text += f"a{tag_name}${tag} = ALargeBitTags;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeBitTags()  # noqa

    for tag in tags:
        instance = CellBuilder().store_bitstring(tag).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{int(tag, 2)}", globals(), locals())


def test_tag_multi_bits_large_zfilled():
    tags = [''.join(tag) for tag in list(product('10', repeat=6))]

    tlb_text = ""

    for tag in tags:
        tag_name = int(tag, 2)
        tlb_text += f"a{tag_name}${tag.zfill(62)} = ALargeBitTagsZfilled;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeBitTagsZfilled()  # noqa

    for tag in tags:
        instance = CellBuilder().store_bitstring(tag.zfill(62)).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{int(tag, 2)}", globals(), locals())


def test_tag_multi_int_large_zfilled():
    tlb_text = ""

    for i in range(64):
        tag = hex(i)[2:].zfill(8)
        tlb_text += f"a{i}#{tag} = ALargeIntTagsFilled;\n"

    add_tlb(tlb_text, globals())
    A_record = ALargeIntTagsFilled()  # noqa

    for i in range(64):
        instance = CellBuilder().store_uint(i, 32).begin_parse()
        exec(f"assert A_record.get_tag(instance) == A_record.Tag.a{i}", globals(), locals())


