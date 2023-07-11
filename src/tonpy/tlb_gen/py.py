from tonpy.libs.python_ton import codegen_python_tlb
from enum import Enum
from tonpy.types import *
from typing import Union, Optional


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

    tlb_text = tlb_text

    old_subclasses = []
    for i in TLBComplex.__subclasses__():
        old_subclasses.append(i)

    exec(parse_tlb(tlb_text), imported_globals, locals())

    # Write new classes to imported globals
    for i in TLBComplex.__subclasses__():
        if i not in old_subclasses:
            print("----" * 10)
            print("FOUND ", i.__name__, " CLASS")
            print("----" * 10)
            imported_globals[i.__name__] = locals()[i.__name__]
