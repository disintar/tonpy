# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path

from tonpy.libs.python_ton import code_dissemble_str
from typing import Union
import os
from tonpy.types import Cell

libs_root = Path(__file__).parents[0]
libs_root = os.path.join(libs_root, 'libs') + os.path.sep


def disassembler(code: Union[Cell, str]):
    if isinstance(code, str):
        return code_dissemble_str(code, str(libs_root))
    elif isinstance(code, Cell):
        return code_dissemble_str(code.to_boc(), str(libs_root))
    else:
        raise ValueError(f"Type {type(code)} is not supported. "
                         f"Please provide cell or string")
