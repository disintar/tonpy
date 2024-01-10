# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path

from tonpy.libs.python_ton import code_dissemble_str, code_dissemble_cell
from typing import Union
import os
from tonpy.types import Cell, VmDict, begin_cell

fift_libs_root = Path(__file__).parents[0]
fift_libs_root = os.path.join(fift_libs_root, 'libs') + os.path.sep


def disassembler(code: Union[Cell, str],
                 libs: Union[Cell, VmDict] = None):
    if libs is None:
        libs = VmDict(256)
        libs.set_builder(0, begin_cell())
        libs = libs.get_cell()
    elif isinstance(libs, VmDict):
        libs = libs.get_cell()

    if isinstance(code, str):
        return code_dissemble_str(code, str(fift_libs_root), libs.cell)
    elif isinstance(code, Cell):
        return code_dissemble_cell(code.cell, str(fift_libs_root), libs.cell)
    else:
        raise ValueError(f"Type {type(code)} is not supported. "
                         f"Please provide cell or string")
