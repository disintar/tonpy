from tonpy import *
from tonpy.tests.block_boc import block_boc
from tonpy.autogen.block import BlockInfo, ValueFlow, BlockExtra, Block
from time import time


def test_block_autogen_unpack():
    c = CellSlice(block_boc, True)

    # block#11ef55aa global_id:int32
    #   info:^BlockInfo value_flow:^ValueFlow
    #   state_update:^(MERKLE_UPDATE ShardState)
    #   extra:^BlockExtra = Block;

    parsed_block = Block().fetch(c)

    # block#11ef55aa global_id:int32
    #   info:^BlockInfo value_flow:^ValueFlow
    #   state_update:^(MERKLE_UPDATE ShardState)
    #   extra:^BlockExtra = Block;
    assert parsed_block.get_tag() == 0x11ef55aa
    assert parsed_block.global_id == -239

    # block_info#9bc7a987 version:uint32
    #   not_master:(## 1)
    #   after_merge:(## 1) before_split:(## 1)
    #   after_split:(## 1)
    #   want_split:Bool want_merge:Bool
    #   key_block:Bool vert_seqno_incr:(## 1)
    #   flags:(## 8) { flags <= 1 }
    #   seq_no:# vert_seq_no:# { vert_seq_no >= vert_seqno_incr }
    #   { prev_seq_no:# } { ~prev_seq_no + 1 = seq_no }
    #   shard:ShardIdent gen_utime:uint32
    #   start_lt:uint64 end_lt:uint64
    #   gen_validator_list_hash_short:uint32
    #   gen_catchain_seqno:uint32
    #   min_ref_mc_seqno:uint32
    #   prev_key_block_seqno:uint32
    #   gen_software:flags . 0?GlobalVersion
    #   master_ref:not_master?^BlkMasterInfo
    #   prev_ref:^(BlkPrevInfo after_merge)
    #   prev_vert_ref:vert_seqno_incr?^(BlkPrevInfo 0)
    #   = BlockInfo;

    block_info = BlockInfo().fetch(parsed_block.info, rec_unpack=True)
    assert block_info.get_tag() == 0x9bc7a987
    assert block_info.version == 0
    assert block_info.not_master == 1
    assert block_info.after_merge == 1
    assert block_info.before_split == 0
    assert block_info.after_split == 0
    assert block_info.want_split == 0
    assert block_info.want_merge == 0
    assert block_info.key_block == 0
    assert block_info.vert_seqno_incr == 0
    assert block_info.flags == 1
    assert block_info.seq_no == 13516764
    assert block_info.vert_seq_no == 1
    assert block_info.gen_utime == 1612979175
    assert block_info.start_lt == 15441606000000
    assert block_info.end_lt == 15441606000117
    assert block_info.gen_validator_list_hash_short == 3566337926
    assert block_info.gen_catchain_seqno == 150640
    assert block_info.min_ref_mc_seqno == 9546494
    assert block_info.prev_key_block_seqno == 9535794

    gen_software = block_info.gen_software
    assert gen_software.capabilities == 46
    assert gen_software.version == 3

    shard = block_info.shard
    assert shard.shard_pfx_bits == 1
    assert shard.workchain_id == 0
    assert shard.shard_prefix == 9223372036854775808

    master_ref = block_info.master_ref
    master = master_ref.master

    assert master.end_lt == 15441605000004
    assert master.seq_no == 9546494
    assert int(master.root_hash, 2) == 0xD98A92A8E06FCE5D2805A447A6DE394060166B3C8D4A0286BFE35740E74FE604
    assert int(master.file_hash, 2) == 0xDCF740947D1C467F3DB482CB049292BDA006C1B052076B3A1F6619773AC378B6

    prev_ref = block_info.prev_ref
    prev1 = prev_ref.prev1
    prev2 = prev_ref.prev2

    assert prev1.end_lt == 15441599000040
    assert prev1.seq_no == 13516763
    assert int(prev1.root_hash, 2) == 0x617F643F15A42F28018E3E3C89F14B952A0D67FA90968AE5360A51B96C6A1C42
    assert int(prev1.file_hash, 2) == 0x563AA5F3D51585B95C0C89BF6C4E39455F4C121269521C1C5B6DC07F03C5D230

    assert int(prev2.root_hash, 2) == 0x032B1BF3016C9B71816C52F207C4CD79D75541F78EACB11CAC2EA7B77D2A603D
    assert int(prev2.file_hash, 2) == 0x8DCAB64721513F3DB73A081DD61CDF51D7FEC79347AB348D43FFB8BC052A8DB3
    assert prev2.end_lt == 15441602000076
    assert prev2.seq_no == 13516699

    # value_flow#b8e48dfb ^[ from_prev_blk:CurrencyCollection
    #   to_next_blk:CurrencyCollection
    #   imported:CurrencyCollection
    #   exported:CurrencyCollection ]
    #   fees_collected:CurrencyCollection
    #   ^[
    #   fees_imported:CurrencyCollection
    #   recovered:CurrencyCollection
    #   created:CurrencyCollection
    #   minted:CurrencyCollection
    #   ] = ValueFlow;

    value_flow = ValueFlow().fetch(parsed_block.value_flow, rec_unpack=True)
    assert value_flow.r1.from_prev_blk.grams.amount.value == 316323479379560897
    assert value_flow.r1.to_next_blk.grams.amount.value == 316323439152031803
    assert value_flow.r1.imported.grams.amount.value == 41877335552
    assert value_flow.r1.exported.grams.amount.value == 76204670704
    assert value_flow.fees_collected.grams.amount.value == 6400193942
    assert value_flow.r2.fees_imported.grams.amount.value == 0
    assert value_flow.r2.recovered.grams.amount.value == 0
    assert value_flow.r2.created.grams.amount.value == 500000000
    assert value_flow.r2.minted.grams.amount.value == 0

    block_extra = BlockExtra().fetch(parsed_block.extra)
    in_msg_descr = block_extra.in_msg_descr
    d = VmDict(256, cell_root=in_msg_descr)

    out_msg_descr = block_extra.out_msg_descr
    account_blocks = block_extra.account_blocks
    assert hex(int(block_extra.rand_seed, 2)).upper()[
           2:] == '80881F1F06B661A89494CE223BE1A491B8461796F01CB2FDF35A1181AEEE3F16'
    assert hex(int(block_extra.created_by, 2)).upper()[
           2:] == 'D318C6BB5F2114B5E37BE9239CDBC5C6F45C5BDFC25DFC6B6B650F7D961CD801'
    custom = block_extra.custom
    assert custom.name == 'Record_nothing'
