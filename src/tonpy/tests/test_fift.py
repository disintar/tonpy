# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.fift import Fift
from tonpy.types.stack import StackEntry


def test_fift():
    a = Fift()
    a.add_lib("TonUtil.fif")
    # language=fift
    a.run("""<b 10 64 u, b>""")

    stack = a.get_stack()
    assert len(stack) == 1
    assert stack[0].get_type() is StackEntry.Type.t_cell
    assert stack[0].get().begin_parse().load_uint(64) == 10


def test_fift_asm():
    a = Fift()
    a.add_lib("Asm.fif")

    # language=fift
    a.run("""<{
  IF:<{
    123456789 PUSHINT
  }>ELSE<{
    x{12345} PUSHSLICE
  }>
  WHILE:<{ ADD }>DO<{
    10 PUSHINT REPEAT:<{
      CONT:<{ NOP }>
      CONT:<{ }>
    }>
  }>
}>s""")

    assert a.last().get_hash() == '0D755E1797E4C709EA72CEC28DA859C689E28D3E0DE4203779439D9739E9FF15'
