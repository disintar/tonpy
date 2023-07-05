from pathlib import Path
import sys
from random import random

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.utils.bit_converter import bitstring_to_utf8


def test_bitstring_to_utf8():
    bitstring = "011000010110001001100011"
    assert bitstring_to_utf8(bitstring) == 'abc'
