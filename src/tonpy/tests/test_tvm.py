from tonpy.fift.fift import convert_assembler
from tonpy.tvm.tvm import TVM
from tonpy.types import Cell, CellSlice, CellBuilder, Stack, StackEntry


def test_simple_tvm():
    # language=fift
    code = convert_assembler("<{ x{0123456789abcdef} PUSHSLICE SHA256U }>c")
    t = TVM(code=code)
    final_stack = t.run()

    assert t.success is True
    assert t.exit_code == -1
    assert t.vm_steps == 3
    assert t.gas_used == 53
    assert t.gas_credit == 0
    assert t.vm_final_state_hash == '0000000000000000000000000000000000000000000000000000000000000000'  # not implemented
    assert t.vm_init_state_hash == '0000000000000000000000000000000000000000000000000000000000000000'
    actions = t.c5_updated.begin_parse()
    assert actions.bits == 0
    assert actions.refs == 0

    assert isinstance(final_stack, Stack)
    assert len(final_stack) == 1
    assert isinstance(final_stack[0], StackEntry)
    assert isinstance(final_stack[0].get(), int)
    assert final_stack[0].get() == 38795098326322736171136434460164583034742468093563686343615948953988372535320


def test_tvm_c4_c5_stack():
    # language=fift
    code = """<{
  ADD
  DEPTH
  c4 PUSH CTOS SBITREFS
  c5 PUSH CTOS SBITREFS 
  <b x{99991111} s, b> PUSHREF c4 POP 
  <b x{aaaabbbb} s, b> PUSHREF c5 POP
  NIL 100 PUSHINT TPUSH 200 PUSHINT TPUSH
  123 PUSHINT
}>c"""

    t = TVM(code=convert_assembler(code),
            data=CellBuilder().store_ref(CellBuilder().end_cell()).store_uint(10, 64).end_cell())
    t.set_stack(Stack([20, 2]))
    final_stack = t.run()
    final_stack = StackEntry.rec_get([i.get() for i in final_stack])
    assert final_stack == [22, 1, 64, 1, 0, 0, [100, 200], 123]
    assert t.c4_updated.begin_parse().to_bitstring() == bin(0x99991111)[2:]
    assert t.c5_updated.begin_parse().to_bitstring() == bin(0xaaaabbbb)[2:]
