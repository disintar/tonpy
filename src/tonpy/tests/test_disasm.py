from tonpy.fift.disasm import disassembler
from tonpy.types.cell import Cell

test1 = """IF:<{
  PUSHINT 123456789
}>ELSE<{
  PUSHSLICE x{12345}
}>
WHILE:<{
  ADD
}>DO<{
  PUSHINT 10
  REPEAT:<{
    CONT:<{
      NOP
    }>
    CONT:<{
    }>
  }>
}>
"""

test2 = """SETCP 0
DICTPUSHCONST 19, (xC_)
DICTIGETJMPZ {
  0 => <{
  }>
  11 => <{
    ADDINT 123
  }>
  12 => <{
    OVER
    EQINT 5
    IFJMP:<{
      NIP
    }>
    MUL
  }>
  13 => <{
    ADD
    CALLDICT 12
  }>
}
THROWARG 11
"""


def test_disassembler():
    c = Cell("te6ccgEBAQEAGgAAMJaCEAdbzRWVizEjRYDikaCWepORAJDk6A==")
    test = disassembler(c)
    print(test)
    assert test == test1


def test_disassembler_str():
    test = disassembler("te6ccgEBAQEAGgAAMJaCEAdbzRWVizEjRYDikaCWepORAJDk6A==")
    assert test == test1


def test_disassembler_2_str():
    test = disassembler("te6ccgEBCAEANAABFP8A9KQT9LzyyAsBAgLPAgMAAdwCASAEBQAF9TPcAgFIBgcADwhwAWRMeCogAAcoPAMg")
    assert test == test2
