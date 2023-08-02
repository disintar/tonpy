from tonpy.libs.python_ton import PyTVM
from tonpy.types import Cell


class TVM:
    def __init__(self, log_level: int = 0,
                 code: Cell = None,
                 data: Cell = None,
                 allow_debug: bool = False,
                 same_c3: bool = True,
                 skip_c7: bool = False):
        self.tvm = PyTVM(log_level, code, data, allow_debug, same_c3, skip_c7)

    def set_state_init(self, state_init: Cell):
        return self.tvm.set_state_init(state_init)

    def set_gas_limit(self, gas_limit=0, gas_max=-1):
        return self.tvm.set_gas_limit(str(gas_limit), str(gas_max))

    def clear_stack(self):
        return self.tvm.clear_stack()

    def run_vm(self):
        return self.tvm.run_vm()

    @property
    def actions(self):
        return self.tvm.actions

    @property
    def new_data(self):
        return self.tvm.new_data

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
        return self.tvm.code

    @code.setter
    def code(self, value):
        self.tvm.code = value

    @property
    def data(self):
        return self.tvm.data

    @data.setter
    def data(self, value):
        self.tvm.data = value
