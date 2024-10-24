# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from typing import Union, List, Optional

from tonpy.libs.python_ton import PyTVM, method_name_to_id as py_method_name_to_id
from tonpy.types import Cell, Stack, StackEntry, VmDict
from tonpy.tvm.c7 import StepInfo, C7


def method_name_to_id(method_name: str):
    """Compute crc for method name, to pass to TVM"""

    return py_method_name_to_id(method_name)


class TVM:
    def __init__(self, log_level: int = 0,
                 code: Union[str, Cell] = None,
                 data: Union[str, Cell] = None,
                 allow_debug: bool = False,
                 same_c3: bool = True,
                 skip_c7: bool = False,
                 enable_stack_dump=True):
        if isinstance(code, str):
            code = Cell(code)

        if isinstance(data, str):
            data = Cell(data)

        self.tvm = PyTVM(log_level,
                         code.cell if code is not None else code,
                         data.cell if data is not None else data,
                         allow_debug,
                         same_c3,
                         skip_c7,
                         enable_stack_dump)
        self.code_hash = code.get_hash()
        self.vm_steps_detailed: Optional[List[StepInfo]] = None
        self.enable_stack_dump = enable_stack_dump
        self.c7 = None

    def set_stack(self, value: Union[Stack, List]) -> None:
        if isinstance(value, list):
            self.tvm.set_stack(Stack(list(reversed(value))).stack)
        else:
            self.tvm.set_stack(value.stack)

    def set_c7(self, value: Union[Union[StackEntry, List], C7]) -> None:
        if isinstance(value, list):
            self.tvm.set_c7(StackEntry(value=value).entry)
        elif isinstance(value, C7):
            self.c7 = value
            self.tvm.set_c7(StackEntry(value=value.to_data()).entry)
        else:
            assert value.get_type() is StackEntry.Type.t_tuple, "C7 must be tuple"
            self.tvm.set_c7(value)

    def set_state_init(self, state_init: Cell) -> bool:
        return self.tvm.set_state_init(state_init)

    def set_unsafe_ignore_chksig(self, chksig: bool):
        self.tvm.set_unsafe_ignore_chksig(chksig)

    def set_gas_limit(self, gas_limit=0, gas_max=-1) -> bool:
        return self.tvm.set_gasLimit(str(gas_limit), str(gas_max))

    def clear_stack(self) -> bool:
        return self.tvm.clear_stack()

    def fetch_detailed_step_info(self) -> None:
        self.vm_steps_detailed = [StepInfo(i) for i in self.tvm.get_stacks()]
        ops = self.tvm.get_ops()
        if len(ops) != len(self.vm_steps_detailed):
            if len(self.vm_steps_detailed) - len(ops) == 1:
                self.vm_steps_detailed = self.vm_steps_detailed[1:]
            else:
                logger.error(f"VM steps: {len(ops)} != {len(self.vm_steps_detailed)}")
                return

        for i, op in enumerate(ops):
            self.vm_steps_detailed[i].next_op = op

    def run(self, unpack_stack=True, allow_non_success=False) -> Union[Stack, List]:
        st = Stack(prev_stack=self.tvm.run_vm())

        if allow_non_success is False:
            assert self.exit_code in [-1, 0], f"TVM run failed with exit code: {self.exit_code} ({self.exit_code_description()})"

        if self.enable_stack_dump:
            self.fetch_detailed_step_info()

        if not unpack_stack:
            return st
        return st.unpack_rec()

    def set_libs(self, libs: VmDict) -> None:
        self.tvm.set_libs(libs.get_cell().cell)

    @property
    def c5_updated(self) -> Cell:
        return Cell(self.tvm.actions)

    @property
    def c4_updated(self) -> Cell:
        return Cell(self.tvm.new_data)

    @property
    def vm_final_state_hash(self) -> str:
        return self.tvm.vm_final_state_hash

    @property
    def vm_init_state_hash(self) -> str:
        return self.tvm.vm_init_state_hash

    @property
    def success(self) -> bool:
        return self.tvm.success

    @property
    def gas_credit(self) -> int:
        return self.tvm.gas_credit

    @property
    def gas_used(self) -> int:
        return self.tvm.gas_used

    @property
    def exit_code(self) -> int:
        # Think of always return ~self.tvm.exit_code
        if self.tvm.exit_code < 0:
            return ~self.tvm.exit_code
        return self.tvm.exit_code

    def exit_code_description(self):
        exit_codes = {
            0: {"Phase": "Compute Phase", "Description": "Standard successful execution exit code."},
            1: {"Phase": "Compute Phase", "Description": "Alternative successful execution exit code."},
            2: {"Phase": "Compute Phase",
                "Description": "Stack underflow. Last op-code consumed more elements than there are on the stacks."},
            3: {"Phase": "Compute Phase",
                "Description": "Stack overflow. More values have been stored on a stack than allowed by this version of TVM."},
            4: {"Phase": "Compute Phase",
                "Description": "Integer overflow. Integer does not fit into −2^256 ≤ x < 2^256 or a division by zero has occurred."},
            5: {"Phase": "Compute Phase", "Description": "Integer out of expected range."},
            6: {"Phase": "Compute Phase",
                "Description": "Invalid opcode. Instruction is unknown in the current TVM version."},
            7: {"Phase": "Compute Phase",
                "Description": "Type check error. An argument to a primitive is of an incorrect value type."},
            8: {"Phase": "Compute Phase",
                "Description": "Cell overflow. Writing to builder is not possible since after operation there would be more than 1023 bits or 4 references."},
            9: {"Phase": "Compute Phase",
                "Description": "Cell underflow. Read from slice primitive tried to read more bits or references than there are."},
            10: {"Phase": "Compute Phase",
                 "Description": "Dictionary error. Error during manipulation with dictionary (hashmaps)."},
            11: {"Phase": "Compute Phase",
                 "Description": "Most often caused by trying to call get-method whose id wasn't found in the code (missing method_id modifier or wrong get-method name specified when trying to call it)."},
            12: {"Phase": "Compute Phase", "Description": "Thrown by TVM in situations deemed impossible."},
            13: {"Phase": "Compute Phase",
                 "Description": "Out of gas error. Thrown by TVM when the remaining gas becomes negative."},
            32: {"Phase": "Action Phase",
                 "Description": "Action list is invalid. Set during action phase if c5 register after execution contains unparsable object."},
            33: {"Phase": "Action Phase", "Description": "Action list is too long."},
            34: {"Phase": "Action Phase",
                 "Description": "Action is invalid or not supported. Set during action phase if current action cannot be applied."},
            35: {"Phase": "Action Phase", "Description": "Invalid Source address in outbound message."},
            36: {"Phase": "Action Phase", "Description": "Invalid Destination address in outbound message."},
            37: {"Phase": "Action Phase",
                 "Description": "Not enough TON. Message sends too much TON (or there is not enough TON after deducting fees)."},
            38: {"Phase": "Action Phase", "Description": "Not enough extra-currencies."},
            40: {"Phase": "Action Phase",
                 "Description": "Not enough funds to process a message. This error is thrown when there is only enough gas to cover part of the message, but does not cover it completely."},
            43: {"Phase": "Action Phase",
                 "Description": "The maximum number of cells in the library is exceeded or the maximum depth of the Merkle tree is exceeded."}
        }

        if self.exit_code in exit_codes:
            return exit_codes[self.exit_code]
        else:
            return ''

    @property
    def vm_steps(self) -> int:
        return self.tvm.vm_steps

    @property
    def code(self) -> Cell:
        return Cell(self.tvm.code)

    @code.setter
    def code(self, value):
        self.tvm.code = value

    @property
    def data(self) -> Cell:
        return Cell(self.tvm.data)

    @data.setter
    def data(self, value):
        self.tvm.data = value
