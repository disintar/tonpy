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
    """
    Compile FunC sources into Fift assembly and optionally convert it to a Cell.

    Args:
        sources: List of FunC source file paths or source strings accepted by the underlying compiler.
        preamble: Include standard preamble in output.
        indent: Indentation size for pretty printing assembly.
        verbosity: Enable verbose compiler output.
        optimization: Optimization level (0..3 depending on compiler support).
        envelope: Wrap result in standard envelope.
        stack_comments: Emit stack comments in assembly.
        op_comments: Emit opcode comments in assembly.
        convert_to_cell: If True, convert produced assembly into a serialized Cell (Fift assembler).

    Returns:
        str: Assembly string or, when convert_to_cell=True, the assembled BOC base64 string produced by Fift.
    """
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
    """
    Compile a FunC source string into Fift assembly and optionally convert it to a Cell.

    Args:
        source: FunC program source as a single string.
        preamble: Include standard preamble in output.
        indent: Indentation size for pretty printing assembly.
        verbosity: Enable verbose compiler output.
        optimization: Optimization level (0..3 depending on compiler support).
        envelope: Wrap result in standard envelope.
        stack_comments: Emit stack comments in assembly.
        op_comments: Emit opcode comments in assembly.
        convert_to_cell: If True, convert produced assembly into a serialized Cell (Fift assembler).

    Returns:
        str: Assembly string or, when convert_to_cell=True, the assembled BOC base64 string produced by Fift.
    """
    result = func_string_to_asm(source, preamble, indent, verbosity, optimization, envelope, stack_comments,
                                op_comments)
    if convert_to_cell:
        result = convert_assembler(result)
    return result
