from pytoniq_core.boc import begin_cell, Cell as PCell
from tonpy import Cell
import random
from time import time

if __name__ == '__main__':
    x = 10 ** 5
    random_bits_1 = []
    random_bits_2 = []

    for i in range(x):
        random_bits_1.append(random.getrandbits(256))
        random_bits_2.append(random.getrandbits(256))

    cells = []
    for i in range(x):
        cells.append(begin_cell()
                     .store_uint(random_bits_1[i], 256)
                     .store_uint(random_bits_1[i], 256)
                     .store_uint(random_bits_1[i], 256)
                     .store_ref(
            begin_cell().store_uint(random_bits_2[i], 256).end_cell()).end_cell().to_boc())

    started_at = time()
    for i in cells:
        Cell(i)
    tonpy_done_at = time() - started_at
    print(f"[TONPY] Loaded {x} cells at: {tonpy_done_at:.2f} seconds")

    started_at = time()
    for i in cells:
        PCell.one_from_boc(i)
    pytoniq_done_at = time() - started_at
    print(f"[PYTONIQ] Loaded {x} cells at: {pytoniq_done_at:.2f} seconds")
    print(f"[DIFF] {abs(tonpy_done_at - pytoniq_done_at):.2f} seconds")
