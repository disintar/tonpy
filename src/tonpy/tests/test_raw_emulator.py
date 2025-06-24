# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys

from tonpy.utils.actions import output_actions_count
from tonpy.autogen.block import MessageAny

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy import Emulator, Cell, VmDict
from tonpy.autogen.block import Account, OutList
from pprint import pprint

from tonpy.data_for_tests.raw_emulator_data_for_test import cfg_test_0, account_state_test_0, message_test_0, \
    cfg_test_2, account_state_test_2, cfg_test_1, account_state_test_1, in_msg_test_1, account_state_test_3


# All txs from mainnet

def test_emulator_internal():
    em = Emulator(VmDict(32, False, cell_root=cfg_test_0))
    account_state = Cell(account_state_test_0)
    success = em.emulate_transaction(
        shard_account=account_state,
        message=Cell(message_test_0),
        unixtime=1687939216,
        lt=38846792000007
    )

    assert success is True
    vm_account = em.account.to_cell()
    cs = vm_account.begin_parse().load_ref(as_cs=True)
    account = Account().fetch(cs, rec_unpack=True)
    assert account.addr.workchain_id == 0
    assert hex(int(account.addr.address, 2))[2:].zfill(
        64).upper() == '5239B71AC50E62C577E626CC12AF146B08B64A4E2E9718FD459C2300E5B205BD'

    assert account.storage.balance.grams.amount.value == 225181653392
    assert account.storage.last_trans_lt == 38846792000010
    assert account.storage.state.x.code.value.get_hash() == 'C12275085EC7DD21925C33A919680186022C6F2A4CED45DBCE3D3E14D438DC0F'
    assert account.storage.state.x.data.value.get_hash() == 'A10C8C4653B1865D4B1ED261EE7D26D6B2B39C719079993E376A173118A01FCF'
    assert account.storage_stat.last_paid == 1687939216
    assert account.storage_stat.used.bits.value == 6757
    assert account.storage_stat.used.cells.value == 20
    assert account.storage_stat.used.public_cells.value == 0
    assert em.transaction.get_hash() == "D5EA7B2B8027AF84501C9D72AADA58AEFDB258B91C3063645CDBC9EB87075313"


def test_emulator_external():
    em = Emulator(VmDict(32, False, cell_root=Cell(cfg_test_1)))
    account_state = Cell(account_state_test_1)
    success = em.emulate_transaction(
        shard_account=account_state,
        unixtime=1696334339,
        lt=41433522000001,
        message=Cell(in_msg_test_1)
    )
    assert success is True
    assert em.transaction.get_hash() == 'EB828263B0BF90320D44DCEF3240BBE08700C8003FD11B3CBA66BF82B4CAA0A0'
    vm_account = em.account.to_cell()
    cs = vm_account.begin_parse().load_ref(as_cs=True)
    account = Account().fetch(cs, rec_unpack=True)

    assert account.addr.workchain_id == 0
    assert hex(int(account.addr.address, 2))[2:].zfill(
        64).upper() == 'D796479201F2C7AFEF411EA75F57E730CAF1E6D4B30C3E38D3952D1914024FFF'

    assert account.storage.balance.grams.amount.value == 993073996
    assert account.storage.last_trans_lt == 41433522000003
    assert account.storage.state.x.code.value.get_hash() == '84DAFA449F98A6987789BA232358072BC0F76DC4524002A5D0918B9A75D2D599'
    assert account.storage.state.x.data.value.get_hash() == 'D91260F27A144AC721A9764EE1EE818DD89D62635F46CF1E65FE5DD1EC6CEE4A'
    assert account.storage_stat.last_paid == 1696334339
    assert account.storage_stat.used.bits.value == 1315
    assert account.storage_stat.used.cells.value == 3
    assert account.storage_stat.used.public_cells.value == 0

    # TODO: understand why in emulator SRC is broken
    actions = OutList(output_actions_count(em.actions)).fetch(em.actions, strict=False, rec_unpack=True)

    assert actions.action.mode == 3
    assert actions.action.out_msg.body.value.get_hash() == '96A296D224F285C67BEE93C30F8A309157F0DAA35DC5B87E410B78630A09CFC7'
    assert actions.action.out_msg.info.bounce is True
    assert actions.action.out_msg.info.bounced is False
    assert actions.action.out_msg.info.created_at == 0
    assert actions.action.out_msg.info.created_lt == 0
    assert hex(int(actions.action.out_msg.info.dest.address, 2))[2:].zfill(
        64).upper() == 'BE0FAA94D4861E2AC3FD4DB28CCE5CA54363D7C69FE4E1424DB3E3650DFF2ECB'
    assert actions.action.out_msg.info.dest.workchain_id == 0
    assert actions.action.out_msg.info.value.grams.amount.value == 6000000000


def test_emulator_tock():
    em = Emulator(VmDict(32, False, cell_root=Cell(cfg_test_2)))
    account_state = Cell(account_state_test_2)
    success = em.emulate_tick_tock_transaction(
        shard_account=account_state,
        unixtime=1696333181,
        lt=41433174000003,
        is_tock=True
    )
    assert success is True
    assert em.transaction.get_hash() == '3A9B185EE049B13FDF071A0AF70CB1B9E3C3C5F758EBDC11A828E1EF36D31D66'
    vm_account = em.account.to_cell()
    cs = vm_account.begin_parse().load_ref(as_cs=True)
    account = Account().fetch(cs, rec_unpack=True)
    assert account.addr.workchain_id == -1
    assert hex(int(account.addr.address, 2))[2:].zfill(
        64).upper() == '5' * 64

    assert account.storage.balance.grams.amount.value == 1637671300957
    assert account.storage.last_trans_lt == 41433174000004
    assert account.storage.state.x.code.value.get_hash() == '64A43970F2007A1DA6D6FC81773CC095D1CC270E81359E471F3B03469ABEB7B5'
    assert account.storage.state.x.data.value.get_hash() == 'EFBEC4D4E8B1FAB1E6A7CE3257350847C8E207F534C6F7FC5B012C0B5BD09F5C'
    assert account.storage_stat.last_paid == 0
    assert account.storage_stat.used.bits.value == 502074
    assert account.storage_stat.used.cells.value == 1927
    assert account.storage_stat.used.public_cells.value == 0


def test_emulator_tick():
    em = Emulator(VmDict(32, False, cell_root=Cell(cfg_test_2)))
    account_state = Cell(account_state_test_3)
    success = em.emulate_tick_tock_transaction(
        shard_account=account_state,
        unixtime=1696334861,
        lt=41433681000001,
        is_tock=False
    )
    assert success is True
    assert em.transaction.get_hash() == 'F2D3A3309F8AF3332249F6DB62B8C65B825474F4234D83389585D1162F3140DF'
