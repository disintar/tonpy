# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

import os

from tonpy.fift import Fift
from tonpy.fift.fift import convert_assembler
from tonpy.func.func import *
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


def test_func_to_asm():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    relative_sources = ['test-nft-item/stdlib.fc',
                        'test-nft-item/params.fc', 
                        'test-nft-item/op-codes.fc', 
                        'test-nft-item/nft-item.fc']
    sources = [os.path.join(script_dir, rel_path) for rel_path in relative_sources]

    cell = func_to_assembler(sources, preamble=True, stack_comments=True, envelope=True)
    assert cell.get_hash() == "BA4D975D2B66231C1F0A0CCCA6E8FF8F7BA0610C4B7639584B8E98303DC3128C"


def test_func_string_to_asm():
    string = """
            const int x = 5;
            const slice s = "abacaba";
            const int y = 3;
            const slice s = "abacaba";
            const int x = 5;
            const int z = 4, z = 4;

            int sdeq (slice s1, slice s2) asm "SDEQ";

            () main() {
                throw_unless(101, x == 5);
                throw_unless(102, y == 3);
                throw_unless(103, z == 4);
                throw_unless(104, sdeq(s, "abacaba"));
            }
            """
    cell = func_string_to_assembler(string)
    assert cell.get_hash() == "456F78EC3453CE253D4CD43F27EF9A9811FA300448C9620B28819C919212B6EC"
