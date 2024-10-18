from traceback import format_exc

from tonpy import StackEntry, add_tlb
from tonpy.tvm import TVM
from loguru import logger

supported_types = [
    'Int8',
    'Int16',
    'Int32',
    'Int64',
    'Int128',
    'Int256',
    'UInt8',
    'UInt16',
    'UInt32',
    'UInt64',
    'UInt128',
    'UInt256',
    'String',
    'FixedString(64)',
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
        elif self.type in ['Slice', 'Cell', 'Continuation', 'Builder'] and self.instance.get('tlb', None):
            tlb = self.instance.get('tlb')

            if 'parse' in tlb:
                data = tlb.get('parse')
                assert isinstance(data, list)

                tmp = {}

                if tlb['dump_with_types']:
                    tmp[f'{self.dton_parse_prefix}{self.name}_type'] = 'String'

                for item in data:
                    path = item.get('path', None)
                    assert path, "Missing path in TLB"

                    path = path.split('.')
                    if tmp.get(path[-1]):
                        raise ValueError(f'Duplicate path {path[-1]}')

                    dtype = item.get('labels', {}).get('dton_type', None)
                    assert dtype in supported_types, f'Unsupported ABI type {dtype}'

                    name = item.get('labels', {}).get('name', path[-1])
                    tmp[f'{self.dton_parse_prefix}{self.name}_{name}'] = dtype

                return tmp

        return {f'{self.dton_parse_prefix}{self.name}': self.dton_type}

    def parse_stack_item(self, stack_entry: StackEntry, tlb_sources) -> dict:
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
            if self.instance.get('tlb', None):
                tlb = self.instance.get('tlb')
                tlb_data = {}
                text = tlb_sources[tlb['id']]['tlb']

                if tlb.get('use_block_tlb'):
                    text = f"{tlb_sources['block_tlb']}\n\n{text}"

                add_tlb(text, tlb_data)
                to_parse = tlb_data[tlb['object']]()

                if stack_entry.get_type() is StackEntry.Type.t_cell:
                    data = to_parse.cell_unpack(stack_entry.get())
                elif stack_entry.get_type() is StackEntry.Type.t_slice:
                    data = to_parse.unpack(stack_entry.get(), True)
                else:
                    item = stack_entry.get().end_cell()
                    data = to_parse.cell_unpack(item, True)

                parsed_data = data.dump(with_types=tlb['dump_with_types'])

                if 'parse' in tlb:
                    data = tlb.get('parse')
                    assert isinstance(data, list)

                    tmp = {}
                    if tlb['dump_with_types']:
                        tmp[f'{self.dton_parse_prefix}{self.name}_type'] = parsed_data['type']

                    for item in data:
                        path = item.get('path', None)
                        assert path, "Missing path in TLB"

                        path = path.split('.')
                        if tmp.get(path[-1]):
                            raise ValueError(f'Duplicate path {path[-1]}')

                        dtype = item.get('labels', {}).get('dton_type', None)
                        assert dtype in supported_types, f'Unsupported ABI type {dtype}'

                        name = item.get('labels', {}).get('name', path[-1])

                        old = parsed_data.get(path[0], None)

                        if len(path) > 1:
                            for item in path[1:]:
                                if old:
                                    old = old.get(item, None)
                        if old is not None:
                            if dtype == 'FixedString(64)':
                                old = hex(old).upper()[2:].zfill(64)

                            tmp[f'{self.dton_parse_prefix}{self.name}_{name}'] = old

                    return tmp
                else:
                    pass

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
        if self.method_args and len(self.method_args) > 0:
            return {}

        tmp = {}

        for getter in self.method_result:
            columns = getter.get_columns()

            for c in columns:
                tmp[f"{self.dton_parse_prefix}{c}"] = columns[c]

        return tmp

    def parse_getters(self, tvm: TVM, tlb_sources) -> dict:
        if self.method_args and len(self.method_args) > 0:
            return {}

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
                tmp.update(getter.parse_stack_item(stack_entry, tlb_sources))
            except Exception as e:
                logger.error(f"Can't parse {getter}: {e}, {format_exc()}")

        return tmp
