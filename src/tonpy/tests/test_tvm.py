# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.fift.fift import convert_assembler
from tonpy.tvm.tvm import TVM, method_name_to_id
from tonpy.types import Cell, CellSlice, CellBuilder, Stack, StackEntry, Continuation, VmDict
import faulthandler

faulthandler.enable()


def test_simple_tvm():
    # language=fift
    code = convert_assembler("<{ x{0123456789abcdef} PUSHSLICE SHA256U }>c")
    t = TVM(code=code)
    final_stack = t.run(unpack_stack=False)

    assert t.success is True
    assert t.exit_code == 0
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
    final_stack = t.run(unpack_stack=False)
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


def test_tvm_c7_complex():
    from tonpy.tvm.c7 import C7
    from c7_data import c7_data

    code = """<{ NOW BLOCKLT LTIME RANDSEED BALANCE }>c"""
    t = TVM(code=convert_assembler(code))
    t.set_c7(C7(time=321, block_lt=999, trans_lt=291, global_config=Cell(c7_data)))

    final_stack = t.run(True)
    assert t.success is True
    assert final_stack[0] == 321
    assert final_stack[1] == 999
    assert final_stack[2] == 291


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
    t = TVM(code=convert_assembler(code), enable_stack_dump=True)
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
    t = TVM(code=convert_assembler(code), enable_stack_dump=True)

    lib_cell = CellBuilder() \
        .store_uint(CellSlice.SpecialType.Library.value, 8) \
        .store_uint(code_hash, 256) \
        .end_cell(special=True)

    t.set_stack([lib_cell])

    libs = VmDict(256)
    libs[code_hash] = cell_code
    t.set_libs(libs)

    final_stack = t.run(unpack_stack=False)
    assert len(t.vm_steps_detailed) == 6
    assert len(final_stack) == 1
    assert final_stack[0].get() == 228


def test_method_name_to_id():
    assert method_name_to_id('get_sale_data') == 72748


def test_set_gas_limit():
    cell_code = convert_assembler("""<{ 228 PUSHINT }>c""")
    t = TVM(code=cell_code)
    t.set_gas_limit(0)
    t.run(allow_non_success=True)
    assert t.exit_code == 13  # out of gas


def test_c7_mutable():
    from tonpy.tvm.c7 import C7
    code = "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"
    data = "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"
    getter = 97904

    tvm = TVM(code=Cell(code), data=Cell(data), enable_stack_dump=True)
    tvm.set_c7(C7(balance_grams=1))
    tvm.set_stack([getter])
    answer = tvm.run(allow_non_success=True)
    print(answer)

    for i in tvm.vm_steps_detailed:
        print(i.next_op, i.stack.unpack_rec())
