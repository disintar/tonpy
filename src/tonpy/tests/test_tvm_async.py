import pytest

from tonpy.fift.fift import convert_assembler
from tonpy.tvm.tvm import TVM
from tonpy.types import Stack, StackEntry


@pytest.mark.asyncio
async def test_simple_tvm_async():
    # language=fift
    code = convert_assembler("<{ x{0123456789abcdef} PUSHSLICE SHA256U }>c")
    t = TVM(code=code)
    final_stack = await t.arun(unpack_stack=False)

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
