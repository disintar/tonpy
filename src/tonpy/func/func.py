from tonpy.libs.python_ton import func_string_to_asm, func_to_asm
from tonpy.fift.fift import convert_assembler


def func_to_assembler(sources: list[str],
                      preamble: bool = False,
                      indent: int = 0,
                      verbosity: bool = False,
                      optimization: int = 2,
                      envelope: bool = True,
                      stack_comments: bool = False,
                      op_comments: bool = False,
                      convert_to_cell: bool = True) -> str:
    result = func_to_asm(sources, preamble, indent, verbosity, optimization, envelope, stack_comments, op_comments)
    if convert_to_cell:
        result = convert_assembler(result)
    return result


def func_string_to_assembler(source: str,
                             preamble: bool = False,
                             indent: int = 0,
                             verbosity: bool = False,
                             optimization: int = 2,
                             envelope: bool = True,
                             stack_comments: bool = False,
                             op_comments: bool = False,
                             convert_to_cell: bool = True) -> str:
    result = func_string_to_asm(source, preamble, indent, verbosity, optimization, envelope, stack_comments,
                                op_comments)
    if convert_to_cell:
        result = convert_assembler(result)
    return result
