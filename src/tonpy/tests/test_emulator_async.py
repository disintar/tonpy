import pytest

from tonpy.types.vmdict import VmDict
from tonpy.tvm.emulator import Emulator
from tonpy.types.cell import Cell
from tonpy.data_for_tests.emulator_data import tx as data


@pytest.mark.asyncio
async def test_emulator_async():
    em = Emulator(Cell(data['config']))
    em.set_rand_seed(data['rand_seed'])
    em.set_prev_blocks_info(data['prev_block_data'])
    em.set_libs(VmDict(256, False, cell_root=Cell(data['libs'])))
    is_tock, now, lt = data['is_tock'], data['now'], data['lt']

    if data['in_msg']:
        await em.aemulate_transaction(
            Cell(data['account_state']),
            Cell(data['in_msg']),
            now,
            lt,
        )
    else:
        await em.aemulate_tick_tock_transaction(
            Cell(data['account_state']),
            is_tock=is_tock,
            unixtime=now,
            lt=lt,
        )

    assert em.transaction.to_cell().get_hash() == Cell(data['transaction']).get_hash()
