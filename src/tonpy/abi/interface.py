from typing import List

from tonpy import TVM
from tonpy.abi.getter import ABIGetterInstance
from loguru import logger


class ABIInterfaceInstance:
    def __init__(self, instance):
        self.instance = instance
        self.name = self.instance["labels"]["name"]

        if 'dton_parse_prefix' not in self.instance['labels']:
            self.dton_parse_prefix = f'parsed_abi_{self.name}_'
        else:
            self.dton_parse_prefix = self.instance['labels']['dton_parse_prefix']

        self.getters = []

        for i in self.instance['get_methods']:
            for getter in self.instance['get_methods'][i]:
                self.getters.append(ABIGetterInstance(getter))

    def __hash__(self):
        return hash(self.instance['labels']['name'])

    def get_columns(self) -> dict:
        columns = {}

        for getter in self.getters:
            tmp = getter.get_columns()
            for c in tmp:
                columns[f"{self.dton_parse_prefix}{c}"] = tmp[c]

        return columns

    def parse_getters(self, tvm: TVM, tlb_sources):
        result = {}

        for getter in self.getters:
            try:
                tmp = getter.parse_getters(tvm, tlb_sources)

                for i in tmp:
                    result[f"{self.dton_parse_prefix}{i}"] = tmp[i]

            except Exception as e:
                logger.warning(f"Can't parse {self.name}, (getter: {getter.method_name}): {e}")

        return result
