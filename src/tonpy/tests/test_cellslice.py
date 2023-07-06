from pathlib import Path
import sys
from random import random

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.cellbuilder import CellBuilder, CellSlice


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
    assert cs.load_uint(32) == 4294967286
    assert cs.bits == 0


def test_to_boc():
    for boc in ["te6ccuEBAQEABgAMAAj////2pzZaHQ==", "te6ccuEBAQEABAAIAAMPtB1ju68="]:
        cs = CellSlice(boc)
        assert cs.to_boc() == boc


def test_load_address():
    cs = CellSlice("te6ccuEBAQEAJABIAEOAHWXV8v1GUyaOAk5BBDDpDrFRBulaV3rnP465NWdH5Gew4RZ/pw==")
    assert cs.load_address() == "EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA"


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
    assert cs.preload_ref(1).load_uint(32) == 3
    assert cs.refs == 3
    cs.skip_refs(1, True)
    assert cs.preload_ref(1).load_uint(32) == 3
    assert cs.refs == 2
    cs.load_ref()
    assert cs.refs == 1
    assert cs.load_ref().load_uint(32) == 3


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

    assert cs.advance_ext(bits_to_skip * (2 ** 16) + refs_to_skip) is True
    assert cs.refs == 2
    assert cs.bits == 240
    assert cs.advance_ext(480 * (2 ** 16) + 0) is False
    assert cs.advance_ext(2 * (2 ** 16) + 4) is False


def test_dump_as_tlb():
    # addr_extern$01 len:(## 9) external_address:(bits len)
    #         = MsgAddressExt;

    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert cs.dump_as_tlb("MsgAddressExt") == "(addr_extern len:10 external_address:xFFE_)"


def test_load_tlb():
    # TODO: more tests
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert cs.bits == 21

    parsed_cs = cs.load_tlb("MsgAddressExt")
    assert parsed_cs.bits == 21

    assert cs.bits == 0


def test_repr():
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    assert str(cs) == "<CellSlice Cell bits: 0..21; refs: 0..0>"


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
