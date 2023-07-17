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
    assert rec_b.test_bool is True
    assert rec_b.cell_unpack(test_b_c) is True


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
    tc = tA.cell_unpack(test_b_c)
    tcs = tA.unpack(test_b_cs)

    assert type(tc) is A.Record_b
    assert tc.get_tag_enum() == A.Tag.b
    assert tc.get_tag() == 16
    assert tc.get_tag_len() == 5
    assert tc.test_bool is True
    assert type(tcs) is A.Record_b
    assert tcs.get_tag_enum() == A.Tag.b
    assert tcs.get_tag() == 16
    assert tcs.get_tag_len() == 5
    assert tcs.test_bool is True

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

    rec = C().fetch(cb.end_cell(), rec_unpack=True)
    assert rec.a.a == 321
    assert rec.a.b.a == 12345


def test_builtin_unpack():
    # language=tl-b
    tlb_text = """
    _ a:^(uint256) b:^(int256) c:^(## 32)  = C;
    _ a:^Cell b:^Any c:^(bits256) d:^C = B;
    _ a:^# b:^(#< 5) c:^(#<= 10) d:^B = A;
    """
    add_tlb(tlb_text, globals())

    cb = CellBuilder

    A_a = cb().store_uint(1, 32).end_cell()
    A_b = cb().store_uint_less(5, 2).end_cell()
    A_c = cb().store_uint_leq(10, 3).end_cell()

    B_a = cb().store_bitstring('1001').end_cell()
    B_b = cb().store_bitstring('0110').end_cell()
    B_c = cb().store_bitstring('1' * 256).end_cell()

    C_a = cb().store_uint(4, 256).end_cell()
    C_b = cb().store_int(5, 256).end_cell()
    C_c = cb().store_uint(6, 32).end_cell()

    final_C = cb().store_ref(C_a).store_ref(C_b).store_ref(C_c).end_cell()
    final_B = cb().store_ref(B_a).store_ref(B_b).store_ref(B_c).store_ref(final_C).end_cell()
    final_A = cb().store_ref(A_a).store_ref(A_b).store_ref(A_c).store_ref(final_B).end_cell()

    rec = A().fetch(final_A, rec_unpack=True)

    assert rec.a == 1
    assert rec.b == 2
    assert rec.c == 3
    assert rec.d.a.begin_parse().to_bitstring() == '1001'
    assert rec.d.b.begin_parse().to_bitstring() == '0110'
    assert rec.d.c == '1' * 256
    assert rec.d.d.a == 4
    assert rec.d.d.b == 5
    assert rec.d.d.c == 6
