from tonpy import CellSlice


def output_actions_count(actions_list: CellSlice):
    i = 0

    while True:
        if actions_list.refs > 0:
            actions_list = actions_list.preload_ref(as_cs=True)
            i += 1
        else:
            return i
