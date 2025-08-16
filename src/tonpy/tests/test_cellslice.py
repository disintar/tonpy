# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys
from random import random

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell


# Warning: CellSlice(cb.to_boc()) is slow
# We use it just for tests, please, use cb.begin_parse() instead

def test_cs_bits():
    for bits in range(1023):
        cb = CellBuilder()
        cb.store_bitstring('1' * bits)

        cs = CellSlice(cb.to_boc())
        assert cs.bits == bits


def test_refs():
    for c_cnt in range(4):

        cb = CellBuilder()
        for i in range(c_cnt):
            cb_in = CellBuilder()
            cb_in.store_zeroes(i)
            cb.store_ref(cb_in.end_cell())
        cs = CellSlice(cb.to_boc())
        assert cs.refs == c_cnt


def test_size_ext():
    cb = CellBuilder()
    cb.store_libref(0)
    cb.store_uint(10, 64)
    cs = cb.begin_parse()
    refs = cs.size_ext() // (2 ** 16)
    bits = cs.size_ext() % 2 ** 16
    assert refs == 1
    assert bits == 64
    cs.load_subslice_ext(cs.size_ext())
    assert cs.empty_ext() is True


def test_load_int():
    for bits in range(2, 256):
        cb = CellBuilder()
        max_int = int('1' * (bits - 1), 2)
        min_int = -1 * int('1' * (bits - 1), 2)
        random_int_pos = int(''.join(['1' if random() > 0.5 else '0' for _ in range(bits - 1)]), 2)
        random_int_neg = -1 * int(''.join(['1' if random() > 0.5 else '0' for _ in range(bits - 1)]), 2)

        cb.store_int(min_int, bits)
        cb.store_int(max_int, bits)
        cb.store_int(random_int_pos, bits)
        cb.store_int(random_int_neg, bits)

        cs = CellSlice(cb.to_boc())

        assert cs.load_int(bits) == min_int
        assert cs.load_int(bits) == max_int
        assert cs.load_int(bits) == random_int_pos
        assert cs.load_int(bits) == random_int_neg


def test_load_uint():
    for bits in range(1, 256):
        cb = CellBuilder()
        max_int = int('1' * bits, 2)
        min_int = int('0' * bits, 2)
        random_int_pos = int(''.join(['1' if random() > 0.5 else '0' for _ in range(bits)]), 2)
        random_int_neg = int(''.join(['1' if random() > 0.5 else '0' for _ in range(bits)]), 2)

        cb.store_uint(min_int, bits)
        cb.store_uint(max_int, bits)
        cb.store_uint(random_int_pos, bits)
        cb.store_uint(random_int_neg, bits)

        cs = CellSlice(cb.to_boc())

        assert cs.load_uint(bits) == min_int

        assert cs.load_uint(bits) == max_int
        assert cs.load_uint(bits) == random_int_pos
        assert cs.load_uint(bits) == random_int_neg


def test_to_bitstring():
    for bits in range(1024):
        cb = CellBuilder()
        random_bits = ''.join(['1' if random() > 0.5 else '0' for _ in range(bits)])
        cb.store_bitstring(random_bits)

        cs = CellSlice(cb.to_boc())
        assert cs.to_bitstring() == random_bits


def test_load_var_int():
    # More tests in store_var_int
    cs = CellSlice("te6ccuEBAQEABAAIAAMPtB1ju68=")
    assert cs.load_var_int(32) == -10


def test_load_var_uint():
    # More tests in store_var_uint
    cs = CellSlice("te6ccuEBAQEABAAIAAMPtB1ju68=")
    assert cs.load_var_uint(32) == 246


def test_preload_int():
    cs = CellSlice("te6ccuEBAQEABgAMAAj////2pzZaHQ==")
    assert cs.preload_int(32) == -10
    assert cs.bits == 32
    assert cs.load_int(32) == -10
    assert cs.bits == 0


def test_preload_uint():
    cs = CellSlice("te6ccuEBAQEABgAMAAj////2pzZaHQ==")
    assert cs.preload_uint(32) == 4294967286
    assert cs.bits == 32


def test_to_boc():
    for boc in ["te6ccuEBAQEABgAMAAj////2pzZaHQ==", "te6ccuEBAQEABAAIAAMPtB1ju68="]:
        cs = CellSlice(boc)
        assert cs.to_boc() == boc


def test_load_address():
    cb = CellBuilder("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    cb.store_uint(10, 256)
    cs = cb.end_cell().begin_parse()

    assert cs.load_address().serialize() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"
    assert cs.bits == 256
    assert cs.load_uint(256) == 10


def test_bit_at():
    bits = "1110001"

    cb = CellBuilder()
    cb.store_bitstring(bits)

    cs = CellSlice(cb.to_boc())

    for position, bit in enumerate(bits):
        assert cs.bit_at(position) == int(bit)


def test_get_hash():
    cs = CellSlice("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    assert cs.get_hash() == '94804DD004BE8628522901CF117E4B03CF69E78FC0A9E92BC578BCCB1B3FD0D2'


def test_load_string():
    # other tests in `test_store_string`
    cb = CellBuilder()
    my_text = "Test string goes here it will be vey long! " * 256
    cb.store_string(my_text)

    cs = CellSlice(cb.to_boc())
    assert cs.load_string() == my_text


def test_skip_bits():
    cb = CellBuilder()
    cb.store_bitstring("1" * 20 + "00")
    cs = CellSlice(cb.to_boc())

    assert cs.bits == 22
    cs.skip_bits(10)
    assert cs.bits == 12
    cs.skip_bits(2, True)
    assert cs.bits == 10
    assert cs.to_bitstring() == "1111111111"
    cs.skip_bits(10)
    assert cs.bits == 0


def test_skip_refs():
    # This is also test for `(pre)load_ref`
    cb = CellBuilder()
    cb.store_ref(CellBuilder().store_uint(1, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(2, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(3, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(4, 32).end_cell())
    cs = cb.begin_parse()

    assert cs.refs == 4
    cs.skip_refs(1)
    assert cs.preload_ref(1, as_cs=True).load_uint(32) == 3
    assert cs.refs == 3
    cs.skip_refs(1, True)
    assert cs.preload_ref(1, as_cs=True).load_uint(32) == 3
    assert cs.refs == 2
    cs.load_ref()
    assert cs.refs == 1
    assert cs.load_ref(as_cs=True).load_uint(32) == 3


def get_test_cell_slice():
    cb = CellBuilder()
    cb.store_ref(CellBuilder().store_uint(1, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(2, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(3, 32).end_cell())
    cb.store_ref(CellBuilder().store_uint(4, 32).end_cell())
    cb.store_uint(0, 32)
    cb.store_uint(10, 64)
    cb.store_uint(101, 128)
    cb.store_uint(1011, 256)

    return CellSlice(cb.to_boc())


def test_advance():
    cs = get_test_cell_slice()
    assert cs.bits == 480
    assert cs.advance(100) is True
    assert cs.bits == 380
    assert cs.advance(381) is False
    assert cs.advance(379)
    assert cs.bits == 1
    assert cs.advance(2) is False


def test_advance_refs():
    cs = get_test_cell_slice()
    assert cs.refs == 4
    assert cs.advance_refs(1) is True
    assert cs.refs == 3
    assert cs.advance_refs(4) is False
    assert cs.advance_refs(2)
    assert cs.refs == 1
    assert cs.advance_refs(2) is False


def test_advance_bit_refs():
    cs = get_test_cell_slice()

    assert cs.refs == 4
    assert cs.bits == 480
    assert cs.advance_bits_refs(240, 2) is True
    assert cs.refs == 2
    assert cs.bits == 240
    assert cs.advance_bits_refs(240, 4) is False
    assert cs.advance_bits_refs(480, 1) is False
    assert cs.refs == 2
    assert cs.bits == 240
    assert cs.advance_bits_refs(240, 2) is True
    assert cs.refs == 0
    assert cs.bits == 0


def test_advance_ext():
    cs = get_test_cell_slice()

    assert cs.refs == 4
    assert cs.bits == 480

    refs_to_skip = 2
    bits_to_skip = 240

    assert cs.advance_ext(refs_to_skip * (2 ** 16) + bits_to_skip) is True
    assert cs.refs == 2
    assert cs.bits == 240
    assert cs.advance_ext(0 * (2 ** 16) + 480) is False
    assert cs.advance_ext(4 * (2 ** 16) + 2) is False


def test_dump_as_tlb():
    # addr_extern$01 len:(## 9) external_address:(bits len)
    #         = MsgAddressExt;

    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert cs.dump_as_tlb("MsgAddressExt") == "(addr_extern len:10 external_address:xFFE_)"


def test_load_tlb():
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert cs.bits == 21

    parsed_cs = cs.load_tlb("MsgAddressExt")
    assert isinstance(parsed_cs, CellSlice)
    assert parsed_cs.bits == 21
    assert cs.bits == 0

    cs = CellSlice(
        'te6ccuECCAEAAQQAAIQAjgEqAXYBwAHaAfQCCAR3z/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhCBfsAAAAAAAAAAAAA9CRYRWORgkrp4QDPAAQIDBAIBIAUGAJj/ACDdIIIBTJe6lzDtRNDXCx/gpPJggQIA1xgg1wsf7UTQ0x/T/9FRErryoSL5AVQQRPkQ8qL4AAHTHzHTB9TRAfsApMjLH8v/ye1UAEgAAAAAInD34ELxa10vhOqvdN1yb+DzIU+uDbmPyYEcko17en0BQ6ABou71BWd19blXL/OtY90qcdH7KByhd6Xhx0cw7MsuUTgHABW+AAADvLNnDcFVUAAVv////7y9GpSiABAAD6usq62rrKuobhGMyA==')
    cs.skip_bits(1, False)  # account$1

    assert cs.bits == 472
    address = cs.load_tlb("MsgAddressInt")
    assert address.bits == 267
    assert cs.bits == 205

    storage_info = cs.load_tlb("StorageInfo")
    assert storage_info.bits == 66
    assert cs.bits == 139

    account_storage = cs.load_tlb("AccountStorage")
    assert account_storage.bits == 139
    assert cs.bits == 0

    account_storage.skip_bits(64, False)
    account_storage.load_tlb("CurrencyCollection")
    assert account_storage.bits == 6


def test_repr():
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert str(
        cs) == "<CellSlice [21] bits, [0] refs, [235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6] hash>"


def test_dump():
    cb = CellBuilder()
    cb.store_uint(0, 10)

    cs = CellSlice(cb.to_boc())
    assert cs.dump()[:-1] == "x{002_}"


def test_bselect():
    mask = 0b1111
    for i, tag in enumerate(['00', '01', '10', '11']):
        cb = CellBuilder()
        cb.store_bitstring(tag)

        cs = CellSlice(cb.to_boc())
        d = cs.bselect(2, mask)
        assert i == d

    mask = 0b1011
    for i, tag in enumerate(['00', '01', '11']):
        cb = CellBuilder()
        cb.store_bitstring(tag)

        cs = CellSlice(cb.to_boc())
        d = cs.bselect(2, mask)
        assert i == d


def test_bselect_ext():
    mask = 0b1101
    for i, tag in enumerate(['0', '1', '11']):
        cb = CellBuilder()

        cb.store_bitstring(tag)

        cs = CellSlice(cb.to_boc())
        d = cs.bselect_ext(2, mask)
        assert i == d


def test_empty_ext():
    cb = CellBuilder()
    cb.store_bitstring('11100')
    cb.store_ref(CellBuilder().end_cell())
    cs = cb.begin_parse()

    assert cs.empty_ext() is False
    cs.load_uint(5)
    assert cs.empty_ext() is False
    cs.load_ref()
    assert cs.empty_ext() is True


def test_load_bool():
    cb = CellBuilder()
    cb.store_uint(1, 1)
    cs = cb.begin_parse()

    assert cs.load_bool() is True
    assert cs.bits == 0

    cb = CellBuilder()
    cb.store_uint(0, 1)
    cs = cb.begin_parse()

    assert cs.load_bool() is False
    assert cs.bits == 0


def test_preload_bool():
    cb = CellBuilder()
    cb.store_uint(1, 1)
    cs = cb.begin_parse()

    assert cs.preload_bool() is True
    assert cs.bits == 1

    cb = CellBuilder()
    cb.store_uint(0, 1)
    cs = cb.begin_parse()

    assert cs.preload_bool() is False
    assert cs.bits == 1


def test_load_less():
    for i in range(0, 100):
        cb = CellBuilder()
        cb.store_uint_less(100, i)
        cs = cb.begin_parse()
        assert cs.load_uint_less(100) == i


def test_load_leq():
    for i in range(0, 101):
        cb = CellBuilder()
        cb.store_uint_leq(100, i)
        cs = cb.begin_parse()
        assert cs.load_uint_leq(100) == i


def test_load_subslice():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    cb.store_ref(CellBuilder().end_cell())
    cs = cb.begin_parse()
    cs.load_uint(16)
    cs2 = cs.load_subslice(16, 1)
    assert cs.bits == 0
    assert cs.refs == 0
    assert cs2.bits == 16
    assert cs2.refs == 1


def test_preload_subslice():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    cb.store_ref(CellBuilder().end_cell())
    cs = cb.begin_parse()
    cs.load_uint(16)
    cs2 = cs.preload_subslice(16, 1)
    cs.load_uint(8)
    assert cs.bits == 8
    assert cs.refs == 1
    assert cs2.bits == 16
    assert cs2.refs == 1


def test_load_bitstring():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    cs = cb.begin_parse()
    cs.load_uint(16)

    bs = cs.load_bitstring(8)
    assert bs == '00000000'
    assert cs.bits == 32 - (8 + 16)
    bs = cs.preload_bitstring(8)
    assert bs == '00001010'
    assert cs.bits == 32 - (8 + 16)


def test_c_cs():
    c = Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    h = c.get_hash()
    cs = c.begin_parse()
    cs.load_uint(2)
    assert cs.get_hash() != h
    assert c.get_hash() == h
    cs2 = c.begin_parse()
    assert cs2.get_hash() == h


def test_load_subslice_ext():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    cb.store_ref(CellBuilder().end_cell())
    cs = cb.begin_parse()
    cs.load_uint(16)
    cs2 = cs.load_subslice_ext(1 * (2 ** 16) + 16)
    assert cs.bits == 0
    assert cs.refs == 0
    assert cs2.bits == 16
    assert cs2.refs == 1


def test_preload_subslice_ext():
    cb = CellBuilder()
    cb.store_uint(10, 32)
    cb.store_ref(CellBuilder().end_cell())
    cs = cb.begin_parse()
    cs.load_uint(16)
    cs2 = cs.preload_subslice_ext(1 * (2 ** 16) + 16)
    cs.load_uint(8)
    assert cs.bits == 8
    assert cs.refs == 1
    assert cs2.bits == 16
    assert cs2.refs == 1


def test_copy_cut_tail():
    cs = CellBuilder().store_bitstring("11100").begin_parse()
    tmp_cs = cs.copy()
    tmp_cs.skip_bits(3)
    cs.cut_tail(tmp_cs)
    assert cs.load_uint(3) == 0b111
    assert tmp_cs.load_uint(2) == 0b00
