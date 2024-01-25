from tonpy.autogen.block import Transaction
from tonpy.types.vmdict import VmDict
from tonpy.tvm.emulator import Emulator
from tonpy.tvm.not_native.emulator_extern import EmulatorExtern
from tonpy.types.cell import Cell
from tonpy.tests.emulator_data import tx as data


# from deepdiff import DeepDiff


# def get_diff(tx1, tx2):
#     tx1_tlb = Transaction()
#     tx1_tlb = tx1_tlb.cell_unpack(tx1, True).dump()
#
#     tx2_tlb = Transaction()
#     tx2_tlb = tx2_tlb.cell_unpack(tx2, True).dump()
#
#     diff = DeepDiff(tx1_tlb, tx2_tlb).to_dict()
#
#     address = tx1_tlb['account_addr']
#     del tx1_tlb
#     del tx2_tlb
#
#     return diff, address


def test_emulator():
    em = Emulator(Cell(data[
                           'config']))  # EmulatorExtern("/Users/tvorogme/projects/ton-disintar/build/emulator/libemulator.dylib", Cell(data['config']))
    em.set_rand_seed(data['rand_seed'])
    em.set_prev_blocks_info(data['prev_block_data'])
    em.set_libs(VmDict(256, False, cell_root=Cell(data['libs'])))
    is_tock, now, lt = data['is_tock'], data['now'], data['lt']

    if data['in_msg']:
        em.emulate_transaction(
            Cell(data['account_state']),
            Cell(data['in_msg']),
            now,
            lt)
    else:
        em.emulate_tick_tock_transaction(
            Cell(data['account_state']),
            is_tock=is_tock,
            unixtime=now,
            lt=lt
        )

    assert em.transaction.to_cell().get_hash() == Cell(data['transaction']).get_hash()
    # print(get_diff(em.transaction.to_cell(), Cell(data['transaction'])))
