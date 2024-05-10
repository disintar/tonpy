# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.fift.fift import convert_assembler
from tonpy.libs.python_ton import func_string_to_asm, func_to_asm


def test_func_to_asm():
    sources = ['src/tonpy/tests/test-nft-item/stdlib.fc',
               'src/tonpy/tests/test-nft-item/params.fc', 
               'src/tonpy/tests/test-nft-item/op-codes.fc', 
               'src/tonpy/tests/test-nft-item/nft-item.fc']
    asm = func_to_asm(sources)
    cell = convert_assembler(asm)
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
    asm = func_string_to_asm(string)
    cell = convert_assembler(asm)
    assert cell.get_hash() == "456F78EC3453CE253D4CD43F27EF9A9811FA300448C9620B28819C919212B6EC"