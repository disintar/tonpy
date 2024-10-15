from tonpy import StackEntry
from tonpy.tvm import TVM
from loguru import logger

supported_types = [
    'UInt8',
    'UInt16',
    'UInt32',
    'UInt64',
    'UInt128',
    'UInt256',
    'String',
    'Address',
    'Datetime'
]


class ABIGetterResultInstance:
    def __init__(self, instance):
        self.instance = instance

        self.labels = self.instance['labels'] if self.instance['labels'] is not None else {}
        self.metadata = self.instance['metadata'] if self.instance['metadata'] is not None else {}

        self.name = self.labels.get('name')
        self.dton_type = self.labels.get('dton_type', self.instance['type'])
        self.type = self.instance['type']
        self.required = self.instance['required']

        if self.dton_type == 'Int':
            self.dton_type = 'UInt256'
        elif self.dton_type in ['Slice', 'Cell', 'Continuation', 'Builder']:
            if self.labels.get('address'):
                self.dton_type = 'Address'
            else:
                self.dton_type = 'String'
        elif self.dton_type == 'Null':
            self.dton_type = 'UInt8'

        if self.dton_type != 'Tuple':
            assert self.dton_type in supported_types, f'Unsupported ABI type {self.dton_type}'
        else:
            self.dton_type = None
            self.items = self.instance['items']

        if 'dton_parse_prefix' not in self.labels:
            self.dton_parse_prefix = f''
        else:
            self.dton_parse_prefix = self.labels['dton_parse_prefix']

    def get_columns(self):
        if self.dton_type == 'Address':
            return {
                f'{self.dton_parse_prefix}{self.name}_workchain': 'Int16',
                f'{self.dton_parse_prefix}{self.name}_address': 'FixedString(64)',
                f'{self.dton_parse_prefix}{self.name}_type': 'String',
            }
        else:
            return {f'{self.dton_parse_prefix}{self.name}': self.dton_type}

    def parse_stack_item(self, stack_entry: StackEntry) -> dict:
        if self.dton_type == 'Address':
            if stack_entry.get_type() is StackEntry.Type.t_cell:
                address = stack_entry.as_cell().begin_parse().load_address()
            elif stack_entry.get_type() is StackEntry.Type.t_slice:
                address = stack_entry.as_cell_slice().load_address()
            elif stack_entry.get_type() is StackEntry.Type.t_builder:
                address = stack_entry.as_cell_builder().end_cell().begin_parse().load_address()

            return {
                f'{self.dton_parse_prefix}{self.name}_workchain': address.workchain,
                f'{self.dton_parse_prefix}{self.name}_address': address.address,
                f'{self.dton_parse_prefix}{self.name}_type': address.type,
            }
        elif self.type in ['Slice', 'Cell', 'Continuation', 'Builder']:
            return {f"{self.dton_parse_prefix}{self.name}": stack_entry.get().to_boc()}
        elif self.dton_type in ['UInt8', 'UInt16', 'UInt32', 'UInt64', 'UInt128', 'UInt256']:
            return {
                f"{self.dton_parse_prefix}{self.name}":
                    stack_entry.as_uint(int(self.dton_type.replace('UInt', '')))}
        elif self.dton_type == 'Datetime':
            return {
                f"{self.dton_parse_prefix}{self.name}": stack_entry.as_uint(64)
            }
        else:
            raise ValueError(f'Unsupported ABI type {self.dton_type}')


class ABIGetterInstance:
    def __init__(self, instance):
        self.instance = instance

        self.method_name = instance['method_name']
        self.method_id = instance['method_id']

        self.method_args = instance['method_args']
        self.method_args_hash = instance['method_args_hash']

        self.method_result = [ABIGetterResultInstance(i) for i in instance['method_result']]
        self.method_result_hash = instance['method_result_hash']
        self.labels = instance['labels'] if instance['labels'] is not None else {}
        self.metadata = instance['metadata'] if instance['metadata'] is not None else {}

        self.result_strict_type_check = instance['result_strict_type_check']
        self.result_length_strict_check = instance['result_length_strict_check']

        if 'dton_parse_prefix' not in self.labels:
            self.dton_parse_prefix = f''
        else:
            self.dton_parse_prefix = self.labels['dton_parse_prefix']

    def get_columns(self):
        tmp = {}

        for getter in self.method_result:
            columns = getter.get_columns()

            for c in columns:
                tmp[f"{self.dton_parse_prefix}{c}"] = columns[c]

        return tmp

    def parse_getters(self, tvm: TVM) -> dict:
        tvm.set_stack([self.method_id])
        stack = tvm.run(allow_non_success=True, unpack_stack=False)

        if self.result_length_strict_check:
            assert len(stack) == len(self.method_result)

        if self.result_strict_type_check:
            my_result_hash = stack.get_abi_hash()
            assert my_result_hash == self.method_result_hash

        tmp = {}

        for getter, stack_entry in zip(self.method_result, stack):
            try:
                tmp.update(getter.parse_stack_item(stack_entry))
            except Exception as e:
                logger.error(f"Can't parse {getter}: {e}")

        return tmp
