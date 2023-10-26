# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.cellbuilder import CellBuilder, Cell
from random import randint


def test_store_ref():
    cb = CellBuilder()
    c = Cell("te6ccuEBAQEAAgAEAABmLc6k")  # empty cell

    assert cb.refs == 0
    assert cb.remaining_refs == 4

    cb.store_ref(c)

    assert cb.refs == 1
    assert cb.remaining_refs == 3


def get_tester_store_builder_or_cellslice(store_builder: bool = False):
    cb1 = CellBuilder()
    cb1.store_ref(Cell("te6ccuEBAQEAAgAEAABmLc6k"))
    cb1.store_uint(32, 64)

    if not store_builder:
        cb1 = cb1.begin_parse()

    bits_cb1 = cb1.bits
    refs_cb1 = cb1.refs

    assert bits_cb1 == 64
    assert refs_cb1 == 1

    cb2 = CellBuilder()
    cb2.store_uint(0, 256)

    bits_cb2 = cb2.bits
    refs_cb2 = cb2.refs

    assert bits_cb2 == 256
    assert refs_cb2 == 0

    if not store_builder:
        cb2.store_slice(cb1)
    else:
        cb2.store_builder(cb1)

    assert cb2.bits == (bits_cb1 + bits_cb2)
    assert cb2.refs == (refs_cb1 + refs_cb2)


def test_store_builder():
    get_tester_store_builder_or_cellslice(True)


def test_store_cell_slice():
    get_tester_store_builder_or_cellslice(False)


def test_store_uint():
    cb = CellBuilder()

    cb.store_uint(0, 1)
    cb.store_uint(1, 64)
    cb.store_uint(int("1" * 64, 2), 64)  # Max uint 64
    cb.store_uint(int("1" * 256, 2), 256)  # Max uint 256

    cs = cb.begin_parse()
    assert cs.load_uint(1) == 0
    assert cs.load_uint(64) == 1
    assert cs.load_uint(64) == int("1" * 64, 2)
    assert cs.load_uint(256) == int("1" * 256, 2)


def test_store_int():
    cb = CellBuilder()

    cb.store_int(0, 1)
    cb.store_int(-1, 2)
    cb.store_int(-1 * int("1" * 63, 2), 64)  # Min int 64
    cb.store_int(int("1" * 63, 2), 64)  # Max int 64
    cb.store_int(int("1" * 256, 2), 257)  # Max int 256
    cb.store_int(-1 * int("1" * 256, 2), 257)  # Max int 64

    cs = cb.begin_parse()
    assert cs.load_int(1) == 0
    assert cs.load_int(2) == -1
    assert cs.load_int(64) == -1 * int("1" * 63, 2)
    assert cs.load_int(64) == int("1" * 63, 2)
    assert cs.load_int(257) == int("1" * 256, 2)
    assert cs.load_int(257) == -1 * int("1" * 256, 2)


def test_store_zeroes():
    cb = CellBuilder()

    cb.store_zeroes(64)
    cb.store_zeroes(128)
    cb.store_zeroes(64)

    cs = cb.begin_parse()
    assert cs.load_uint(64 + 128 + 64) == 0
    assert cs.bits == 0 and cs.refs == 0


def test_store_ones():
    cb = CellBuilder()

    cb.store_ones(32)
    cb.store_ones(64)
    cb.store_ones(128)
    cb.store_ones(256)

    cs = cb.begin_parse()
    assert cs.load_uint(32 + 64 + 128) == int("1" * (32 + 64 + 128), 2)
    assert cs.load_uint(256) == int("1" * 256, 2)
    assert cs.bits == 0 and cs.refs == 0


def test_store_uint_less():
    cb = CellBuilder()
    cb.store_uint_less(int("1" * 32, 2), 0)
    cb.store_uint_less(int("1" * 32, 2), int("1" * 31, 2))
    cb.store_uint_less(int("1" * 30, 2), 0)
    cb.store_uint_less(int("1" * 30, 2), 32123123)
    cb.store_uint_less(3, 2)

    cs = cb.begin_parse()
    assert cs.load_uint(32) == 0
    assert cs.load_uint(32) == int("1" * 31, 2)
    assert cs.load_uint(30) == 0
    assert cs.load_uint(30) == 32123123
    assert cs.load_uint(len(bin(3)[2:])) == 2


def test_store_uint_leq():
    cb = CellBuilder()

    cb.store_uint_leq(int("1" * 32, 2), 0)
    cb.store_uint_leq(int("1" * 32, 2), int("1" * 32, 2))
    cb.store_uint_leq(int("1" * 30, 2), 0)
    cb.store_uint_leq(int("1" * 30, 2), int("1" * 30, 2))

    x = 100000
    y = x - 1

    cb.store_uint_leq(x, y)

    cs = cb.begin_parse()
    assert cs.load_uint(32) == 0
    assert cs.load_uint(32) == int("1" * 32, 2)
    assert cs.load_uint(30) == 0
    assert cs.load_uint(30) == int("1" * 30, 2)
    assert cs.load_uint(len(bin(x)[2:])) == y


def test_store_bitstring():
    cb = CellBuilder()
    cb.store_bitstring('1111')
    cs = cb.begin_parse()
    assert cs.load_uint(4) == int('1' * 4, 2)

    cb = CellBuilder()
    cb.store_bitstring(''.join(['0' if x % 2 == 0 else '1' for x in range(1023)]))
    cs = cb.begin_parse()
    assert cs.bits == 1023

    bits = bin(2268)[2:]
    cb = CellBuilder()
    cb.store_bitstring(bits)
    cs = cb.begin_parse()
    assert cs.load_uint(len(bits)) == 2268


def test_get_cell():
    cell = Cell("te6ccuEBAQEAAgAEAABmLc6k")
    cb = CellBuilder()
    assert cb.end_cell().to_boc() == cell.to_boc()


def test_dump():
    cb = CellBuilder()
    cb.store_uint(0, 10)
    assert cb.dump()[:-1] == "x{002_}"


def test_dump_as_tlb():
    cb = CellBuilder()

    # addr_extern$01 len:(## 9) external_address:(bits len)
    #         = MsgAddressExt;

    cb.store_bitstring("01")
    cb.store_uint(10, 9)
    cb.store_bitstring("1" * 10)
    assert cb.dump_as_tlb("MsgAddressExt") == "(addr_extern len:10 external_address:xFFE_)"


def test_get_hash():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    assert cb.get_hash() == "8AE53B8B0178198B1165839BF91623AD7A92E1D074F1C3786A62078542667024"

    cb = CellBuilder()
    cb.store_ref(CellBuilder().end_cell())
    assert cb.get_hash() == "6C64B3153333F7AF728149B88CD7B27F5DED7CD17AC88893EE47FC208A15E640"


def test_repr():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    assert str(
        cb) == "<CellBuilder [32] bits, [0] refs, [8AE53B8B0178198B1165839BF91623AD7A92E1D074F1C3786A62078542667024] hash>"


def test_store_grams():
    for i in range(30):
        cb = CellBuilder()

        grams = randint(0, int("1" * 16, 2))
        cb.store_grams(grams)
        boc32_grams = cb.end_cell().to_boc()

        cb = CellBuilder()
        cb.store_var_uint(grams, 16)
        boc32 = cb.end_cell().to_boc()

        assert boc32_grams == boc32

    cb = CellBuilder()
    grams = int("1" * 16, 2)
    cb.store_grams(grams)
    boc32_grams = cb.end_cell().to_boc()

    cb = CellBuilder()
    cb.store_var_uint(grams, 16)
    boc32 = cb.end_cell().to_boc()

    assert boc32_grams == boc32


def test_store_var_uint():
    cb = CellBuilder()

    x = 32
    bits = ((x - 1) * 8)
    int_by_bits = int("1" * bits, 2)

    cb.store_var_uint(int_by_bits, x)  # max value can be stored
    assert cb.bits == (len(bin(x)[2:]) + bits - 1)

    cs = cb.begin_parse()
    assert cs.load_var_uint(x) == int_by_bits

    cb = CellBuilder()
    cb.store_var_uint(0, 16)
    cs = cb.begin_parse()
    assert cs.load_var_uint(16) == 0

    cb = CellBuilder()
    cb.store_var_uint(352, 16)
    cs = cb.begin_parse()
    assert cs.load_var_uint(16) == 352


def test_store_var_int():
    cb = CellBuilder()

    x = 32
    bits = ((x - 1) * 8)
    int_by_bits = -1 * int("1" * (bits - 1), 2)

    cb.store_var_int(int_by_bits, x)  # max value can be stored
    assert cb.bits == (len(bin(x)[2:]) + bits - 1)

    cs = cb.begin_parse()
    assert cs.load_var_int(x) == int_by_bits

    cb = CellBuilder()
    x = 32
    bits = ((x - 1) * 8)
    int_by_bits = int("1" * (bits - 1), 2)

    cb.store_var_int(int_by_bits, x)  # max value can be stored
    assert cb.bits == (len(bin(x)[2:]) + bits - 1)

    cs = cb.begin_parse()
    assert cs.load_var_int(x) == int_by_bits

    cb = CellBuilder()
    cb.store_var_int(-1, 16)
    cs = cb.begin_parse()
    assert cs.load_var_int(16) == -1

    cb = CellBuilder()
    cb.store_var_int(-352, 16)
    cs = cb.begin_parse()
    assert cs.load_var_int(16) == -352

    cb = CellBuilder()
    cb.store_var_int(352, 16)
    cs = cb.begin_parse()
    assert cs.load_var_int(16) == 352


def test_store_address():
    cb = CellBuilder()
    cb.store_address("EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA")
    assert cb.bits == 267
    cs = cb.begin_parse()
    assert cs.load_address().serialize() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"

    cb = CellBuilder()
    cb.store_address("UQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPTmF")
    assert cb.bits == 267
    cs = cb.begin_parse()
    assert cs.load_address().serialize() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"

    cb = CellBuilder()
    cb.store_address("0:EB2EAF97EA32993470127208218748758A88374AD2BBD739FC75C9AB3A3F233D")
    assert cb.bits == 267
    cs = cb.begin_parse()
    assert cs.load_address().serialize() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"


def test_store_string():
    s_to_store = "Hello world!"
    cb = CellBuilder()
    cb.store_string(s_to_store)
    cs = cb.begin_parse()
    my_string = cs.load_string()
    assert my_string == s_to_store

    cb = CellBuilder()
    large_text = "Test string goes here it will be vey long! " * 2000
    cb.store_string(large_text)
    cs = cb.begin_parse()

    text_parsed = cs.load_string()
    assert text_parsed == large_text

    cb = CellBuilder()
    text = "Allow to fetch by size: [will not be loaded]"
    cb.store_string(text)
    cs = cb.begin_parse()
    assert text[:23] == cs.load_string(23 * 8)

    # TODO: test not strict load


def test_store_build():
    cb = CellBuilder()
    cb.store_bool(True)
    cs = cb.begin_parse()
    assert cs.load_bool() is True

    cb = CellBuilder()
    cb.store_bool(False)
    cs = cb.begin_parse()
    assert cs.load_bool() is False
