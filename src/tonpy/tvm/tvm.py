from tonpy.libs.python_ton import PyTVM
from tonpy.types import Cell, Stack, StackEntry


class TVM:
    def __init__(self, log_level: int = 0,
                 code: Cell = None,
                 data: Cell = None,
                 allow_debug: bool = False,
                 same_c3: bool = True,
                 skip_c7: bool = False):
        self.tvm = PyTVM(log_level,
                         code.cell if code is not None else code,
                         data.cell if data is not None else data,
                         allow_debug,
                         same_c3,
                         skip_c7)

    def set_stack(self, value: Stack):
        self.tvm.set_stack(value.stack)

    def set_state_init(self, state_init: Cell):
        return self.tvm.set_state_init(state_init)

    def set_gas_limit(self, gas_limit=0, gas_max=-1):
        return self.tvm.set_gas_limit(str(gas_limit), str(gas_max))

    def clear_stack(self):
        return self.tvm.clear_stack()

    def run(self):
        return Stack(prev_stack=self.tvm.run_vm())

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
