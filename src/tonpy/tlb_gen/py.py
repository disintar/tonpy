# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path

from tonpy.libs.python_ton import codegen_python_tlb
from enum import Enum
from tonpy.types import *
from typing import Union, Optional
from loguru import logger


def parse_tlb(tlb_text: str) -> str:
    """
    Parse TLB and generate Python Class objects for tlb

    :param tlb_text: TLB code
    :return: Python code that have been generated
    """

    code = codegen_python_tlb(tlb_text)

    return code


def add_tlb(tlb_text: str,
            imported_globals: globals):
    """
    Parse & Run generated python code, so after that you can operate with new loaded class objects

    :param tlb_text: TLB code
    :return:
    """

    tlb_text = parse_tlb(tlb_text).split("# definitions of constants")
    constants, tlb_text = tlb_text[1], tlb_text[0]

    # Debug
    tlb_text_t = tlb_text.split("\n")
    for i, j in zip(range(len(tlb_text_t)), tlb_text_t):
        print(i, ": ", j)

    exec(tlb_text, globals(), locals())

    # Write new classes to imported globals
    for i in locals()['tlb_classes']:
        print("Found class: ", i)
        imported_globals[i] = locals()[i]
        globals()[i] = locals()[i]

    exec(constants, globals(), locals())


def process_file(filepath: str, out_path: str = None) -> None:
    """
    Parse tlb file and convert it to ``.py`` file with codegened code

    :param filepath: Path to ``.tlb`` file to convert to
    :return:
    """

    file_path = Path(filepath)

    with open(file_path) as f:
        data = f.read()
        tlb_code = parse_tlb(data)

        if out_path is None:
            new_path = Path(filepath.replace(file_path.name, file_path.name[:-4] + '.py'))
        else:
            new_path = out_path

        logger.warning(f"New path for TLB gen: {new_path}")
        with open(new_path, 'w') as fw:
            fw.write(tlb_code)
