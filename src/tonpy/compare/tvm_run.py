# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0
import sys

from tonpy.fift.fift import convert_assembler
from tonpy.tvm.tvm import TVM
from tonpy.types import Cell
import faulthandler
import pytest
import asyncio
from time import time
import multiprocessing
from tonpy.tvm.c7 import C7
from tqdm import tqdm
from tonpy.tests.c7_data import c7_data
from tonpy.scheduler import init_thread_scheduler

faulthandler.enable()


def f(params):
    index, code, c7_entry = params  # Unpack arguments
    if isinstance(c7_entry, Cell):
        c7_entry = C7(time=321, block_lt=999, trans_lt=291, global_config=c7_entry).to_stack_entry()

    # Create TVM instance inside process
    tvm = TVM(code=code)
    tvm.set_c7(c7_entry)
    tvm.set_gas_limit(5000000, 5000000)

    final_stack = tvm.run(True, allow_non_success=True)
    assert tvm.success is False
    return True


async def af(tvm_instance):
    final_stack = await tvm_instance.arun(True, allow_non_success=True)
    assert tvm_instance.success is False
    return True


def run_multiprocessing(num_instances, code, c7_data):
    params = [(i, code, c7_data) for i in range(num_instances)]  # Generate args for processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(f, params, chunksize=1)
    return results


@pytest.mark.asyncio
async def test_tvm_c7_complex(cs, mode):
    init_thread_scheduler(30)

    code = """<{ ZERO ZERO WHILE:<{ 1 INT }>DO<{ DUP }> }>c"""
    num_instances = cs

    code = convert_assembler(code)
    c7_cell = Cell(c7_data)
    c7_entry = C7(time=321, block_lt=999, trans_lt=291, global_config=c7_cell).to_stack_entry()

    ### asyncSYNC RUN**
    if mode == 'async':
        tvms = [TVM(code=code) for _ in range(num_instances)]
        for tvm in tvms:
            tvm.set_c7(c7_entry)
            tvm.set_gas_limit(5000000, 5000000)

        started_at = time()
        futures = [af(tvm) for tvm in tvms]
        results = await asyncio.gather(*futures)
        assert all(results)

        print(f"[ASYNC] Run {num_instances} TVMs at: {time() - started_at:.2f} seconds")

    ### **SYNC RUN**
    if mode == 'sync':
        started_at = time()
        results = [f((i, code, c7_entry)) for i in range(num_instances)]
        assert all(results)
        print(f"[SYNC] Run {num_instances} TVMs at: {time() - started_at:.2f} seconds")

    ### **MULTIPROCESSING RUN**
    if mode == 'multiprocessing':
        started_at = time()
        results = run_multiprocessing(num_instances, code.copy(), c7_cell)
        assert all(results)
        print(f"[MULTIPROCESSING] Run {num_instances} TVMs at: {time() - started_at:.2f} seconds")


if __name__ == '__main__':
    mode = sys.argv[-1]
    cs = int(sys.argv[-2])

    loop = asyncio.new_event_loop()
    loop.run_until_complete(test_tvm_c7_complex(cs, mode))
