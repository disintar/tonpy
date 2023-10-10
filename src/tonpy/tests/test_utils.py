from pathlib import Path
import sys
from random import random
from tonpy.utils.address_packer import pack_address

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.utils.bit_converter import bitstring_to_utf8


def test_bitstring_to_utf8():
    bitstring = "011000010110001001100011"
    assert bitstring_to_utf8(bitstring) == 'abc'


def test_pack_address():
    cs = pack_address("EQDrLq-X6jKZNHAScgghh0h1iog3StK71zn8dcmrOj8jPWRA")
    assert cs.get_hash() == '94804DD004BE8628522901CF117E4B03CF69E78FC0A9E92BC578BCCB1B3FD0D2'

    from tonpy.autogen.block import MsgAddress
    loaded = MsgAddress().fetch(cs)
    address = loaded.to_dict(rec_unpack=True)
    assert address['x']['workchain_id'] == 0
    assert hex(int(address['x']['address'], 2))[2:].zfill(
        64).upper() == 'EB2EAF97EA32993470127208218748758A88374AD2BBD739FC75C9AB3A3F233D'
