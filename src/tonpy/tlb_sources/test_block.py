from tonpy import *
import base64 as b
from tonpy.tlb_sources.block import Block
from time import time


def test_block_tlb():
    start = time()
    with open("raw-13516764.bin", 'rb') as f:
        bb = b.b64encode(f.read())
        c = CellSlice(bb.decode(), True)

    rec = Block().fetch(c, True)
    print("\n", time() - start)
    print(rec)
