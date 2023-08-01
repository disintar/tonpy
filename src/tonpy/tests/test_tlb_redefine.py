from tonpy.tlb_gen.py import add_tlb
from tonpy.types import CellBuilder

def test_builtin_unpack():
    # language=tl-b
    tlb_text = """
    _ a:^(uint256) b:^(int256) c:^(## 32)  = C;
    _ a:^Cell b:^Any c:^(bits256) d:^C = B;
    _ a:^# b:^(#< 5) c:^(#<= 10) d:^B = A;
    """
    add_tlb(tlb_text, globals())

    A_a = CellBuilder().store_uint(1, 32).end_cell()
    A_b = CellBuilder().store_uint_less(5, 2).end_cell()
    A_c = CellBuilder().store_uint_leq(10, 3).end_cell()

    B_a = CellBuilder().store_bitstring('1001').end_cell()
    B_b = CellBuilder().store_bitstring('0110').end_cell()
    B_c = CellBuilder().store_bitstring('1' * 256).end_cell()

    C_a = CellBuilder().store_uint(4, 256).end_cell()
    C_b = CellBuilder().store_int(5, 256).end_cell()
    C_c = CellBuilder().store_uint(6, 32).end_cell()

    final_C = CellBuilder().store_ref(C_a).store_ref(C_b).store_ref(C_c).end_cell()
    final_B = CellBuilder().store_ref(B_a).store_ref(B_b).store_ref(B_c).store_ref(final_C).end_cell()
    final_A = CellBuilder().store_ref(A_a).store_ref(A_b).store_ref(A_c).store_ref(final_B).end_cell()
    assert final_A.get_hash() == '8FC752179C5AD3870CD9A70A205548E8F7389B865316707339DFA33875F0808A'

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

