from typing import Union, List, Optional

from tonpy.libs.python_ton import PyTVM, method_name_to_id as py_method_name_to_id
from tonpy.types import Cell, Stack, StackEntry, VmDict


def method_name_to_id(method_name: str):
    """Compute crc for method name, to pass to TVM"""

    return py_method_name_to_id(method_name)


class StepInfo:
    stack: Stack = None
    gas_consumed: int = None
    gas_remaining: int = None
    next_op: str = None

    def __init__(self, stack_info):
        self.stack = Stack(prev_stack=stack_info.stack)
        self.gas_consumed = int(stack_info.gas_consumed)
        self.gas_remaining = int(stack_info.gas_remaining)
        self.next_op = None


class TVM:
    def __init__(self, log_level: int = 0,
                 code: Cell = None,
                 data: Cell = None,
                 allow_debug: bool = False,
                 same_c3: bool = True,
                 skip_c7: bool = False,
                 enable_stack_dump=True):
        self.tvm = PyTVM(log_level,
                         code.cell if code is not None else code,
                         data.cell if data is not None else data,
                         allow_debug,
                         same_c3,
                         skip_c7,
                         enable_stack_dump)
        self.vm_steps_detailed: Optional[List[StepInfo]] = None
        self.enable_stack_dump = enable_stack_dump

    def set_stack(self, value: Union[Stack, List]):
        if isinstance(value, list):
            self.tvm.set_stack(Stack(list(reversed(value))).stack)
        else:
            self.tvm.set_stack(value.stack)

    def set_c7(self, value: Union[StackEntry, List]):
        if isinstance(value, list):
            self.tvm.set_c7(StackEntry(value=value).entry)
        else:
            assert value.get_type() is StackEntry.Type.t_tuple, "C7 must be tuple"
            self.tvm.set_c7(value)

    def set_state_init(self, state_init: Cell):
        return self.tvm.set_state_init(state_init)

    def set_gas_limit(self, gas_limit=0, gas_max=-1):
        return self.tvm.set_gas_limit(str(gas_limit), str(gas_max))

    def clear_stack(self):
        return self.tvm.clear_stack()

    def fetch_detailed_step_info(self):
        self.vm_steps_detailed = [StepInfo(i) for i in self.tvm.get_stacks()]
        ops = self.tvm.get_ops()
        assert len(ops) == len(self.vm_steps_detailed)
        for i, op in enumerate(ops):
            self.vm_steps_detailed[i].next_op = op

    def run(self, unpack_stack=False):
        st = Stack(prev_stack=self.tvm.run_vm())
        if self.enable_stack_dump:
            self.fetch_detailed_step_info()

        if not unpack_stack:
            return st
        return st.unpack_rec()

    def set_libs(self, libs: VmDict):
        self.tvm.set_libs(libs.get_cell().cell)

    @property
    def c5_updated(self):
        return Cell(self.tvm.actions)

    @property
    def c4_updated(self):
        return Cell(self.tvm.new_data)

    @property
    def vm_final_state_hash(self):
        return self.tvm.vm_final_state_hash

    @property
    def vm_init_state_hash(self):
        return self.tvm.vm_init_state_hash

    @property
    def success(self):
        return self.tvm.success

    @property
    def gas_credit(self):
        return self.tvm.gas_credit

    @property
    def gas_used(self):
        return self.tvm.gas_used

    @property
    def exit_code(self):
        return self.tvm.exit_code

    @property
    def vm_steps(self):
        return self.tvm.vm_steps

    @property
    def code(self):
        return Cell(self.tvm.code)

    @code.setter
    def code(self, value):
        self.tvm.code = value

    @property
    def data(self):
        return Cell(self.tvm.data)

    @data.setter
    def data(self, value):
        self.tvm.data = value
