from tonpy import TVM, add_tlb
from tonpy.abi.getter import ABIGetterInstance
from tonpy.abi.utils import parse_tlb_spec
from loguru import logger
import traceback

class ABIInterfaceInstance:
    def __init__(self, instance):
        self.instance = instance
        self.name = self.instance["labels"]["name"]
        self.tlb_sources__ = None

        if 'dton_parse_prefix' not in self.instance['labels']:
            self.dton_parse_prefix = f'parsed_abi_{self.name}_'
        else:
            self.dton_parse_prefix = self.instance['labels']['dton_parse_prefix']

        self.getters = []
        self.storage = self.instance.get('storage')

        # get_methods could be absent when only storage is provided
        for i in self.instance.get('get_methods', {}):
            for getter in self.instance['get_methods'][i]:
                self.getters.append(ABIGetterInstance(getter))

    def __hash__(self):
        return hash(self.instance['labels']['name'])

    def get_columns(self) -> dict:
        columns = {}

        # getters columns
        for getter in self.getters:
            tmp = getter.get_columns()
            for c in tmp:
                columns[f"{self.dton_parse_prefix}{c}"] = tmp[c]

        # storage columns
        columns.update(self.get_storage_columns())

        return columns

    def get_storage_columns(self) -> dict:
        if not self.storage:
            return {}

        tlb = self.storage
        return parse_tlb_spec(
            None,
            tlb,
            prefix=self.dton_parse_prefix,
            name_prefix="",
            columns_only=True,
        )

    def parse_getters(self, tvm: TVM, tlb_sources):
        result = {}

        for getter in self.getters:
            try:
                tmp = getter.parse_getters(tvm, tlb_sources)

                if tmp is None:
                    return None

                for i in tmp:
                    result[f"{self.dton_parse_prefix}{i}"] = tmp[i]

            except Exception as e:
                logger.warning(f"Can't parse {self.name}, (getter: {getter.method_name}): {e} {traceback.format_exc()}")
                return None # abi should work completely, with a result in each getter

        # parse storage too
        storage_parsed = self.parse_storage(tvm, tlb_sources)
        if storage_parsed:
            result.update(storage_parsed)

        return result

    async def aparse_getters(self, tvm: TVM, tlb_sources):
        result = {}

        # can't do gether because of diffrent stack
        for getter in self.getters:
            try:
                tmp = await getter.aparse_getters(tvm, tlb_sources)

                if tmp is None:
                    return None

                for i in tmp:
                    result[f"{self.dton_parse_prefix}{i}"] = tmp[i]

            except Exception as e:
                logger.warning(f"Can't parse {self.name}, (getter: {getter.method_name}): {e} {traceback.format_exc()}")
                return None # abi should work completely, with a result in each getter

        # parse storage too
        storage_parsed = self.parse_storage(tvm, tlb_sources)
        if storage_parsed:
            result.update(storage_parsed)

        return result

    def parse_storage(self, tvm: TVM, tlb_sources):
        if not self.storage:
            return {}

        try:
            tlb = self.storage
            # resolve TLB text
            tlb_text = None
            if 'id' in tlb and tlb['id'] in tlb_sources:
                tlb_text = tlb_sources[tlb['id']]['tlb']
            elif 'file_path' in tlb and tlb['file_path'] in tlb_sources:
                tlb_text = tlb_sources[tlb['file_path']]['tlb']

            if tlb.get('use_block_tlb'):
                tlb_text = f"{tlb_sources['block_tlb']}\n\n{tlb_text}"

            env = {}
            add_tlb(tlb_text, env)
            to_parse = env[tlb['object']]()

            # Unpack the contract storage cell
            data = to_parse.cell_unpack(tvm.data, True)
            dumped = data.dump(with_types=tlb.get('dump_with_types', False))

            return parse_tlb_spec(
                dumped,
                tlb,
                prefix=self.dton_parse_prefix,
                name_prefix="",
                columns_only=False,
            )
        except Exception as e:
            logger.warning(f"Can't parse storage for {self.name}: {e} {traceback.format_exc()}")
            return {}

