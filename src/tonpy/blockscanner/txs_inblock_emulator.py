from tonpy import Emulator, VmDict, Cell


def emulate_in_block(data):
    out = []
    block, account_state, txs = data
    config = block['key_block']['config']

    em = Emulator(config)
    em.set_rand_seed(block['rand_seed'])
    prev_block_data = [list(reversed(block['prev_block_data'][0])), block['prev_block_data'][1]]
    em.set_prev_blocks_info(prev_block_data)
    em.set_libs(VmDict(256, False, cell_root=Cell(block['libs'])))

    for tx in txs:
        current_tx_cs = tx['tx'].begin_parse()
        lt = tx['lt']
        now = tx['now']
        is_tock = tx['is_tock']

        tmp = current_tx_cs.load_ref(as_cs=True)

        if tmp.load_bool():
            in_msg = tmp.load_ref()
        else:
            in_msg = None

        if in_msg is None:
            success = em.emulate_tick_tock_transaction(
                account_state,
                is_tock,
                now,
                lt
            )
        else:
            # Emulate
            success = em.emulate_transaction(
                account_state,
                in_msg,
                now,
                lt)

        account_state = em.account.to_cell()
        out.append([tx, account_state.copy()])

    return out
