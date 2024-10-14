from collections import defaultdict
from typing import List

from tonpy.tvm import TVM
from tonpy.abi.interface import ABIInterfaceInstance
from loguru import logger

class ABIInstance:
    def __init__(self, abi_data):
        self.abi_data = abi_data

        self.by_code_hash = defaultdict(set)
        self.by_get_method = defaultdict(set)
        self.by_name = {}

        for (i, j) in abi_data['by_name'].items():
            self.by_name[i] = ABIInterfaceInstance(j)

        for code_hash in abi_data['by_code_hash']:
            for name in abi_data['by_code_hash'][code_hash]:
                self.by_code_hash[code_hash].add(self.by_name[name])

        for get_method in abi_data['by_get_method']:
            for name in abi_data['by_get_method'][get_method]:
                self.by_get_method[get_method].add(self.by_name[name])

    def get_columns(self):
        columns = {}

        for interface in self.by_name.values():
            columns.update(interface.get_columns())

        return columns

    def abi_for_getters(self, getters: List[int]):
        tmp = set()

        for getter in getters:
            tmp.add(self.by_get_method[getter])

        return tmp

    def parse_getters(self, tvm: TVM, getters: List[int] = None):
        parsers = set()

        if tvm.code_hash in self.by_code_hash:
            for parser in self.by_code_hash[tvm.code_hash]:
                parsers.add(parser)
        else:
            if getters is not None:
                for parser in self.abi_for_getters(getters):
                    parsers.add(parser)
            else:
                logger.warning("Code hash not found in ABI, provide getters for parse methods")

        result = {}

        for parser in parsers:
            result.update(parser.parse_getters(tvm))

        return result
