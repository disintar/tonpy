# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

import os
from pathlib import Path

from tonpy import Cell
from tonpy.libs.python_ton import PyFift
from tonpy.types import Stack

libs_root = Path(__file__).parents[0]
libs_root = os.path.join(libs_root, 'libs') + os.path.sep


class Fift:
    def __init__(self, base_path=None, silent=True):
        """

        :param base_path: Path to libs folder
        :param silent: Print output to std::out
        """
        if base_path is None:
            base_path = libs_root

        self.fift = PyFift(base_path, silent)

    def add_lib(self, lib: str) -> None:
        """Add lib to load"""
        self.fift.add_lib(lib)

    def clear_libs(self) -> None:
        """Clear all loaded libs"""
        self.fift.clear_libs()

    def run(self, code_text: str) -> int:
        """Run fift code, return exit_code"""
        return self.fift.run(code_text)

    def get_stack(self) -> Stack:
        return Stack(prev_stack=self.fift.get_stack())

    def last(self):
        return self.get_stack()[0].get()


def convert_assembler(assembler_code: str) -> Cell:
    f = Fift()
    f.add_lib("Asm.fif")
    f.run(assembler_code)
    return f.last()

