from collections import defaultdict
from typing import List, Callable

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
            tmp.update(self.by_get_method[str(getter)])

        return tmp

    def get_parsers(self, code_hash: str, getters: List[int]):
        parsers = set()

        if code_hash in self.by_code_hash:
            for parser in self.by_code_hash[code_hash]:
                parsers.add(parser)
        else:
            if getters is not None:
                tmp_parsers = set()
                for parser in self.abi_for_getters(getters):
                    parsers.add(parser)
                    tmp_parsers.add(parser)

                self.by_code_hash[code_hash] = tmp_parsers
            else:
                logger.warning("Code hash not found in ABI, provide getters for parse methods")

        return parsers

    def parse_getters(self, tvm: TVM, getters: List[int] = None):
        parsers = self.get_parsers(tvm.code_hash, getters)

        result = {}

        for parser in parsers:
            result.update(parser.parse_getters(tvm))

        return result

    def parse_getter_lazy(self, code_hash, get_tvm: Callable, getters: List[int] = None):
        parsers = self.get_parsers(code_hash, getters)

        result = {}

        if len(parsers) > 0:
            tvm = get_tvm()

            for parser in parsers:
                result.update(parser.parse_getters(tvm))

        return result
