# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.tlb_gen.py import add_tlb
from tonpy.types import CellBuilder


def test_nat_unpack():
    # language=tl-b
    tlb_text = """
    a$10001 a:# b:(#< 10) c:(#<= 64) d:(## 64) = A;
    b$10000 test_bool:(## 1) = A;
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
    test_b = CellBuilder().store_bitstring('10000').store_bool(True)

    test_b_cs = test_b.begin_parse()
    test_b_c = test_b.end_cell()

    add_tlb(tlb_text, globals())

    rec_a = A.Record_a()
    assert rec_a.a is None
    assert rec_a.b is None
    assert rec_a.c is None
    assert rec_a.d is None

    initial_hash = test_a_c.get_hash()
    assert rec_a.unpack(test_a_cs) is True

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)

    # on pack we get same cell
    assert initial_hash == rec_a.cell_pack().get_hash()

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

    initial_hash = test_b_c.get_hash()
    assert rec_b.unpack(test_b_cs) is True
    assert rec_b.test_bool is True
    assert rec_b.cell_unpack(test_b_c) is True

    # on pack we get same cell
    assert initial_hash == rec_b.cell_pack().get_hash()


def test_complex_unpack():
    # language=tl-b
    tlb_text = """
    a$10001 a:# b:(#< 10) c:(#<= 64) d:(## 64) = A;
    b$10000 test_bool:(## 1) = A;
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
    test_b = CellBuilder().store_bitstring('10000').store_bool(True)

    test_b_cs = test_b.begin_parse()
    test_b_c = test_b.end_cell()

    add_tlb(tlb_text, globals())

    tA = A()
    initial_hash = test_b_c.get_hash()
    tc = tA.cell_unpack(test_b_c)
    tcs = tA.unpack(test_b_cs)

    assert type(tc) is A.Record_b
    assert tc.get_tag_enum() == A.Tag.b
    assert tc.get_tag() == 16
    assert tc.get_tag_len() == 5
    assert tc.test_bool is True
    assert tc.cell_pack().get_hash() == initial_hash
    assert type(tcs) is A.Record_b
    assert tcs.get_tag_enum() == A.Tag.b
    assert tcs.get_tag() == 16
    assert tcs.get_tag_len() == 5
    assert tcs.test_bool is True
    assert tcs.cell_pack().get_hash() == initial_hash

    tA = A()
    initial_hash = test_a_c.get_hash()
    rec_a = tA.cell_unpack(test_a_c)

    assert type(rec_a) is A.Record_a
    assert rec_a.get_tag_enum() == A.Tag.a
    assert rec_a.get_tag() == 17
    assert rec_a.get_tag_len() == 5
    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)
    assert rec_a.cell_pack().get_hash() == initial_hash

    rec_a = tA.unpack(test_a_cs)
    assert rec_a.get_tag_enum() == A.Tag.a
    assert rec_a.get_tag() == 17
    assert rec_a.get_tag_len() == 5

    assert rec_a.a == int('1' * 32, 2)
    assert rec_a.b == 9
    assert rec_a.c == 64
    assert rec_a.d == int('1' * 64, 2)
    assert rec_a.cell_pack().get_hash() == initial_hash


def test_complex_unpack():
    # language=tl-b
    tlb_text = """
    _ a:(## 64) = A;
    _ a:# b:^A = B;
    _ a:B = C;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder()  # _ a:B = C;
    cb.store_uint(321, 32)  # _ a:#
    cb.store_ref(CellBuilder().store_uint(12345, 64).end_cell())  # b:^A = B; / _ a:(## 64) = A;
    c = cb.end_cell()

    initial_hash = c.get_hash()
    rec = C().fetch(c, rec_unpack=True)
    assert rec.a.a == 321
    assert rec.a.b.a == 12345

    # on pack we get same cell
    assert initial_hash == rec.cell_pack().get_hash()


def test_bool_tag():
    # language=tl-b
    tlb_text = """
    bool_false$0 = Bool;
    bool_true$1 = Bool;
    _ test_b:Bool = A;
    """
    add_tlb(tlb_text, globals())

    a = CellBuilder().store_zeroes(1).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.test_b is False

    # on pack we get same cell
    assert initial_hash == rec.cell_pack().get_hash()

    a = CellBuilder().store_ones(1).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.test_b is True

    # on pack we get same cell
    assert initial_hash == rec.cell_pack().get_hash()


def test_hex_tag():
    # language=tl-b
    tlb_text = """
    bool_false#00000032 = MyTag;
    bool_true#00000064 = MyTag;
    _ test_b:MyTag = A;
    """
    add_tlb(tlb_text, globals())

    a = CellBuilder().store_uint(0x000000064, 32).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.test_b == 0x000000064
    assert initial_hash == rec.cell_pack().get_hash()

    a = CellBuilder().store_uint(0x000000032, 32).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.test_b == 0x000000032
    assert initial_hash == rec.cell_pack().get_hash()

    # invalid cell
    rec = A().fetch(CellBuilder().store_uint(0x000000016, 32).end_cell())
    assert rec is None


def test_basic_contraint():
    tlb_texts = []

    # language=tl-b
    tlb_texts.append("""
    _ a:# { a >= 10 } { a <= 100 } = A;
    _ b:(#< 100) { b = 99 } = B;
    """)

    # language=tl-b
    tlb_texts.append("""
    _ a:# { 100 >= a } { 10 <= a } = A;
    _ b:(#< 100) { 99 = b } = B;
    """)

    for tlb_text in tlb_texts:
        add_tlb(tlb_text, globals())

        a = CellBuilder().store_uint(11, 32).begin_parse()
        initial_hash = a.get_hash()
        rec = A().fetch(a)
        assert rec.a == 11
        assert rec.cell_pack().get_hash() == initial_hash

        a = CellBuilder().store_uint(9, 32).begin_parse()
        rec = A().fetch(a)
        assert rec is None

        a = CellBuilder().store_uint(99, 32).begin_parse()
        initial_hash = a.get_hash()
        rec = A().fetch(a)
        assert rec.a == 99
        assert rec.cell_pack().get_hash() == initial_hash

        a = CellBuilder().store_uint(101, 32).begin_parse()
        rec = A().fetch(a)
        assert rec is None

        a = CellBuilder().store_uint_less(100, 99).begin_parse()
        initial_hash = a.get_hash()
        rec = B().fetch(a)
        assert rec.b == 99
        assert rec.cell_pack().get_hash() == initial_hash

        rec = B().fetch(CellBuilder().store_uint_less(100, 98).begin_parse())
        assert rec is None


def test_condition_fields():
    # language=tl-b
    tlb_text = """
    _ a:(## 1) b:(a?(## 64)) = A;
    """
    add_tlb(tlb_text, globals())

    a = CellBuilder().store_bool(False).begin_parse()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.a is False
    assert rec.b is None
    assert rec.cell_pack().get_hash() == initial_hash

    a = CellBuilder().store_bool(False).store_uint(180, 64).begin_parse()
    initial_hash = a.get_hash()
    rec = A().fetch(a, strict=False)
    assert rec.a is False
    assert rec.b is None

    # because of strict=False some data will be lost on repack
    assert rec.cell_pack().get_hash() != initial_hash
    assert rec.cell_pack().get_hash() == '90AEC8965AFABB16EBC3CB9B408EBAE71B618D78788BC80D09843593CAC98DA4'

    a = CellBuilder().store_bool(False).store_uint(179, 64).end_cell()
    rec = A().fetch(a)
    assert rec is None

    a = CellBuilder().store_bool(True).store_uint(179, 64).begin_parse()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.a is True
    assert rec.b == 179
    assert rec.cell_pack().get_hash() == initial_hash


def test_conditions_fields_chain():
    # language=tl-b
    tlb_text = """
    _ a:(## 32) b:(## 8) c:(## 1) d:(## 1) e:((a . b)?(c?(d?((## 64))))) = A;
    """
    add_tlb(tlb_text, globals())

    a = CellBuilder().store_uint(int('00000000000000000000100000000000', 2), 32).store_uint(12, 8).store_bool(
        True).store_bool(True).store_uint(1234567, 64).begin_parse()
    initial_hash = a.get_hash()
    rec = A().fetch(a)
    assert rec.e.preload_uint(
        64) == 1234567  # todo: https://github.com/ton-blockchain/ton/issues/736#issuecomment-1638776943
    assert rec.cell_pack().get_hash() == initial_hash


def test_anon_subfields():
    # language=tl-b
    tlb_text = """
    _ a:# ^[ b:# c:# d:# ] = A;
    """
    add_tlb(tlb_text, globals())

    a = CellBuilder().store_uint(1, 32).store_ref(
        CellBuilder().store_uint(2, 32).store_uint(3, 32).store_uint(4, 32).end_cell()).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)

    assert rec.a == 1
    assert rec.r1.b == 2
    assert rec.r1.c == 3
    assert rec.r1.d == 4

    assert rec.cell_pack().get_hash() == initial_hash

    # language=tl-b
    tlb_text = """
    _ a:# ^[ b:# ^[ c:# ^[ d:# ] ] ] = A;
    """
    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(0, 32).end_cell()
    tmp2 = cb().store_uint(1, 32).store_ref(tmp).end_cell()
    tmp3 = cb().store_uint(2, 32).store_ref(tmp2).end_cell()

    a = cb().store_uint(3, 32).store_ref(tmp3).end_cell()
    initial_hash = a.get_hash()
    rec = A().fetch(a)

    assert rec.a == 3
    assert rec.r1.b == 2
    assert rec.r1.r1.c == 1
    assert rec.r1.r1.r1.d == 0
    assert rec.cell_pack().get_hash() == initial_hash


def test_sub_params():
    # language=tl-b
    tlb_text = """
    _ {x:#} a:(## x) = A x;
    _ b:(A 10) = B;
    """
    add_tlb(tlb_text, globals())

    tmp = CellBuilder().store_uint(12, 10).end_cell()
    initial_hash = tmp.get_hash()
    rec = B().fetch(tmp)

    assert rec.b.a == 12
    assert rec.cell_pack().get_hash() == initial_hash


def test_sub_params_complex():
    # language=tl-b
    tlb_text = """
        _ {x:#} {y:#} {z:#} a:(## x) { a = y } 
        b:(## z) { b = z } = A x y z;
        _ b:(A 10 5 8) = B;
        """
    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(5, 10).store_uint(8, 8).end_cell()
    initial_hash = tmp.get_hash()
    rec = B().fetch(tmp)

    assert rec.b.a == 5
    assert rec.b.b == 8
    assert rec.cell_pack().get_hash() == initial_hash

    cb = CellBuilder
    tmp = cb().store_uint(5, 10).store_uint(7, 8).end_cell()
    rec = B().fetch(tmp)

    assert rec is None

    cb = CellBuilder
    tmp = cb().store_uint(5, 10).store_uint(7, 8).end_cell()
    rec = B().fetch(tmp, strict=False)

    assert isinstance(rec, B.Record)
    assert rec.b is None


def test_negate_simple():
    # language=tl-b
    tlb_text = """
    _ {a:#} b:# { ~a = 10 } = NegateSimple;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(5, 32).end_cell()
    initial_hash = tmp.get_hash()
    rec = NegateSimple().fetch(tmp)
    assert rec.b == 5
    assert rec.a == 10
    assert rec.cell_pack().get_hash() == initial_hash


def test_negate_simple_plus():
    # language=tl-b
    tlb_text = """
    _ {a:#} b:# { ~a = b } = NegateSimplePlus;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(8, 32).end_cell()
    initial_hash = tmp.get_hash()
    rec = NegateSimplePlus().fetch(tmp)
    assert rec.b == 8
    assert rec.a == 8
    assert rec.cell_pack().get_hash() == initial_hash

    # language=tl-b
    tlb_text = """
    _ {a:#} {ap:#} b:# c:# { ~a = (10 * b) } { ~ap = (10 + c) } = NegateSimplePlus;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(8, 32).store_uint(184, 32).end_cell()
    initial_hash = tmp.get_hash()
    rec = NegateSimplePlus().fetch(tmp)
    assert rec.b == 8
    assert rec.c == 184
    assert rec.a == 80
    assert rec.ap == 194
    assert rec.cell_pack().get_hash() == initial_hash


def test_negate_deduct():
    # language=tl-b
    tlb_text = """
    _ {a:#} {ap:#} b:# c:# { ~a + 10 = b } { ~ap * 20 = c } = NegateDeduct;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(18, 32).store_uint(200, 32).end_cell()
    initial_hash = tmp.get_hash()
    rec = NegateDeduct().fetch(tmp)
    assert rec.b == 18
    assert rec.a == 8
    assert rec.c == 200
    assert rec.ap == 10
    assert rec.cell_pack().get_hash() == initial_hash


def test_negate_complex():
    # language=tl-b
    tlb_text = """
    _ {m:#} {x:#} n:(## m) d:(## x) = Define ~n m x ~d;
    _ {n_from_define:#} {d:#} defined_val:(Define ~n_from_define 8 1 ~d) real_value:(## n_from_define) = Example;
    """

    add_tlb(tlb_text, globals())

    cb = CellBuilder
    tmp = cb().store_uint(16, 8).store_uint(1, 1).store_uint(123, 16).end_cell()
    initial_hash = tmp.get_hash()
    rec = Example().fetch(tmp)

    assert rec.real_value == 123
    assert rec.defined_val.m == 8
    assert rec.defined_val.n == 16
    assert rec.defined_val.x == 1
    assert rec.defined_val.d == 1
    assert rec.cell_pack().get_hash() == initial_hash


def test_apply_on_builtin():
    # language=tl-b
    tlb_text = """
    anycast_info$_ depth:(#<= 30) { depth >= 1 }
    rewrite_pfx:(bits depth) = Anycast;
    """

    add_tlb(tlb_text, globals())

    tmp = CellBuilder().store_uint_leq(30, 5).store_bitstring("1" * 5).begin_parse()
    initial_hash = tmp.get_hash()
    rec = Anycast().fetch(tmp)
    assert rec.depth == 5
    assert rec.rewrite_pfx == "1" * 5
    assert rec.cell_pack().get_hash() == initial_hash
