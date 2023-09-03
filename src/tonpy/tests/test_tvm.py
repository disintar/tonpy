from tonpy.fift.fift import convert_assembler
from tonpy.tvm.tvm import TVM, method_name_to_id
from tonpy.types import Cell, CellSlice, CellBuilder, Stack, StackEntry, Continuation, VmDict


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


def test_tvm_c7():
    code = """<{ NOW BLOCKLT LTIME RANDSEED BALANCE }>c"""
    t = TVM(code=convert_assembler(code))
    t.set_c7([
        None,
        None,
        123,
        321,
        999,
        0x123,
        [50000, CellBuilder().end_cell()],
        CellBuilder().end_cell().begin_parse()])

    final_stack = t.run(True)
    assert t.success is True
    assert final_stack[0] == 321
    assert final_stack[1] == 999
    assert final_stack[2] == 291
    assert final_stack[3][0] == 50000
    assert final_stack[3][1].begin_parse().bits == 0 and final_stack[3][1].begin_parse().refs == 0
    assert final_stack[4].bits == 0 and final_stack[4].refs == 0


def test_tvm_continuation():
    # language=fift
    code = """<{ BLESS CONT:<{ 2 INT }> }>c"""
    t = TVM(code=convert_assembler(code))

    # language=fift
    t.set_stack([convert_assembler("""<{ 228 PUSHINT }>s""")])
    final_stack = t.run(True)

    assert isinstance(final_stack[0], Continuation)
    assert isinstance(final_stack[1], Continuation)

    t = TVM(code=convert_assembler(code))
    # convert continuation to cellslice and run again
    t.set_stack([final_stack[1].serialize().begin_parse()])

    final_stack = t.run(True)
    assert isinstance(final_stack[0], Continuation)
    assert isinstance(final_stack[1], Continuation)


def test_tvm_step_info():
    # language=fift
    code = """<{ BLESS 2 INT }>c"""
    t = TVM(code=convert_assembler(code))
    # language=fift
    t.set_stack([convert_assembler("""<{ 228 PUSHINT }>s""")])
    t.run()

    info = t.vm_steps_detailed
    assert len(info) == 3

    step_0 = info[0]
    assert step_0.next_op == 'execute BLESS\n'
    assert len(step_0.stack) == 1
    assert step_0.stack[0].get().get_hash() == '961254B41350A116E5DC3166307071F29DA1F3A286A144350289ACBE1A64C459'
    assert step_0.gas_consumed == 0
    assert step_0.gas_remaining == 9223372036854775807

    step_1 = info[1]
    assert step_1.next_op == 'execute PUSHINT 2\n'
    assert len(step_1.stack) == 1
    assert isinstance(step_1.stack[0].get(), Continuation)
    assert step_1.gas_consumed == 26
    assert step_1.gas_remaining == 9223372036854775781


def test_tvm_set_libs():
    cell_code = convert_assembler("""<{ 228 PUSHINT }>c""")
    code_hash = int(cell_code.get_hash(), 16)

    # language=fift
    code = """<{ CTOS BLESS EXECUTE  }>c"""
    t = TVM(code=convert_assembler(code))

    lib_cell = CellBuilder() \
        .store_uint(CellSlice.SpecialType.Library.value, 8) \
        .store_uint(code_hash, 256) \
        .end_cell(special=True)

    t.set_stack([lib_cell])

    libs = VmDict(256)
    libs[code_hash] = cell_code
    t.set_libs(libs)

    final_stack = t.run()
    assert len(t.vm_steps_detailed) == 6
    assert len(final_stack) == 1
    assert final_stack[0].get() == 228


def test_method_name_to_id():
    assert method_name_to_id('get_sale_data') == 72748
