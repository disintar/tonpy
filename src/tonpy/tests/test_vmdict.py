# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from pathlib import Path
import sys
from random import random
from time import time

import pytest

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.vmdict import VmDict
from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell
from tonpy.data_for_tests.dict_test_boc import config_44, reveal_dict_boc


def test_vm_dict_from_boc():
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
            83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
            129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
            150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
            171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
            192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
            213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
            234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254,
            255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268]

    values = ['reveal_822.json', 'reveal_841.json', 'reveal_331.json', 'reveal_230.json', 'reveal_572.json',
              'reveal_569.json', 'reveal_1013.json', 'reveal_1094.json', 'reveal_1077.json', 'reveal_329.json',
              'reveal_915.json', 'reveal_979.json', 'reveal_13.json', 'reveal_816.json', 'reveal_591.json',
              'reveal_458.json', 'reveal_273.json', 'reveal_533.json', 'reveal_202.json', 'reveal_954.json',
              'reveal_1092.json', 'reveal_1025.json', 'reveal_526.json', 'reveal_939.json', 'reveal_811.json',
              'reveal_858.json', 'reveal_141.json', 'reveal_556.json', 'reveal_921.json', 'reveal_338.json',
              'reveal_893.json', 'reveal_86.json', 'reveal_33.json', 'reveal_891.json', 'reveal_579.json',
              'reveal_926.json', 'reveal_147.json', 'reveal_379.json', 'reveal_916.json', 'reveal_981.json',
              'reveal_1050.json', 'reveal_810.json', 'reveal_434.json', 'reveal_1051.json', 'reveal_950.json',
              'reveal_987.json', 'reveal_257.json', 'reveal_864.json', 'reveal_940.json', 'reveal_95.json',
              'reveal_920.json', 'reveal_1109.json', 'reveal_246.json', 'reveal_54.json', 'reveal_374.json',
              'reveal_1012.json', 'reveal_1008.json', 'reveal_1032.json', 'reveal_524.json', 'reveal_996.json',
              'reveal_983.json', 'reveal_1110.json', 'reveal_602.json', 'reveal_603.json', 'reveal_909.json',
              'reveal_605.json', 'reveal_606.json', 'reveal_1037.json', 'reveal_608.json', 'reveal_963.json',
              'reveal_1005.json', 'reveal_1102.json', 'reveal_612.json', 'reveal_613.json', 'reveal_919.json',
              'reveal_615.json', 'reveal_813.json', 'reveal_930.json', 'reveal_1067.json', 'reveal_619.json',
              'reveal_988.json', 'reveal_621.json', 'reveal_622.json', 'reveal_1107.json', 'reveal_1082.json',
              'reveal_876.json', 'reveal_626.json', 'reveal_627.json', 'reveal_840.json', 'reveal_1086.json',
              'reveal_1035.json', 'reveal_631.json', 'reveal_1070.json', 'reveal_633.json', 'reveal_634.json',
              'reveal_951.json', 'reveal_883.json', 'reveal_1031.json', 'reveal_1039.json', 'reveal_970.json',
              'reveal_966.json', 'reveal_641.json', 'reveal_642.json', 'reveal_643.json', 'reveal_934.json',
              'reveal_645.json', 'reveal_646.json', 'reveal_1057.json', 'reveal_1087.json', 'reveal_852.json',
              'reveal_957.json', 'reveal_651.json', 'reveal_908.json', 'reveal_653.json', 'reveal_654.json',
              'reveal_655.json', 'reveal_911.json', 'reveal_657.json', 'reveal_658.json', 'reveal_659.json',
              'reveal_1056.json', 'reveal_898.json', 'reveal_662.json', 'reveal_878.json', 'reveal_888.json',
              'reveal_665.json', 'reveal_830.json', 'reveal_953.json', 'reveal_668.json', 'reveal_900.json',
              'reveal_670.json', 'reveal_671.json', 'reveal_1053.json', 'reveal_673.json', 'reveal_1064.json',
              'reveal_675.json', 'reveal_881.json', 'reveal_677.json', 'reveal_678.json', 'reveal_679.json',
              'reveal_1017.json', 'reveal_1000.json', 'reveal_682.json', 'reveal_683.json', 'reveal_684.json',
              'reveal_999.json', 'reveal_849.json', 'reveal_863.json', 'reveal_688.json', 'reveal_689.json',
              'reveal_968.json', 'reveal_1019.json', 'reveal_692.json', 'reveal_1021.json', 'reveal_694.json',
              'reveal_828.json', 'reveal_696.json', 'reveal_831.json', 'reveal_698.json', 'reveal_699.json',
              'reveal_700.json', 'reveal_1076.json', 'reveal_1083.json', 'reveal_703.json', 'reveal_1108.json',
              'reveal_846.json', 'reveal_895.json', 'reveal_947.json', 'reveal_708.json', 'reveal_709.json',
              'reveal_944.json', 'reveal_711.json', 'reveal_935.json', 'reveal_713.json', 'reveal_855.json',
              'reveal_1060.json', 'reveal_716.json', 'reveal_717.json', 'reveal_718.json', 'reveal_867.json',
              'reveal_1042.json', 'reveal_960.json', 'reveal_932.json', 'reveal_723.json', 'reveal_724.json',
              'reveal_725.json', 'reveal_927.json', 'reveal_1071.json', 'reveal_728.json', 'reveal_976.json',
              'reveal_918.json', 'reveal_1074.json', 'reveal_845.json', 'reveal_733.json', 'reveal_984.json',
              'reveal_735.json', 'reveal_736.json', 'reveal_896.json', 'reveal_972.json', 'reveal_739.json',
              'reveal_740.json', 'reveal_741.json', 'reveal_1003.json', 'reveal_835.json', 'reveal_744.json',
              'reveal_824.json', 'reveal_1016.json', 'reveal_985.json', 'reveal_748.json', 'reveal_836.json',
              'reveal_897.json', 'reveal_1038.json', 'reveal_990.json', 'reveal_753.json', 'reveal_754.json',
              'reveal_928.json', 'reveal_756.json', 'reveal_757.json', 'reveal_758.json', 'reveal_759.json',
              'reveal_894.json', 'reveal_761.json', 'reveal_943.json', 'reveal_1084.json', 'reveal_764.json',
              'reveal_843.json', 'reveal_923.json', 'reveal_913.json', 'reveal_1009.json', 'reveal_769.json',
              'reveal_1029.json', 'reveal_937.json', 'reveal_772.json', 'reveal_773.json', 'reveal_1079.json',
              'reveal_1059.json', 'reveal_776.json', 'reveal_861.json', 'reveal_1010.json', 'reveal_779.json',
              'reveal_1081.json', 'reveal_809.json', 'reveal_782.json', 'reveal_946.json', 'reveal_784.json',
              'reveal_844.json', 'reveal_786.json', 'reveal_787.json', 'reveal_788.json', 'reveal_789.json',
              'reveal_790.json', 'reveal_791.json', 'reveal_991.json', 'reveal_812.json', 'reveal_902.json',
              'reveal_795.json', 'reveal_796.json', 'reveal_797.json', 'reveal_798.json', 'reveal_912.json',
              'reveal_901.json', 'reveal_801.json', 'reveal_802.json', 'reveal_803.json', 'reveal_804.json',
              'reveal_1106.json', 'reveal_806.json', 'reveal_833.json', 'reveal_808.json']

    d = VmDict(64, cell_root=reveal_dict_boc)

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]

    d = VmDict(64, cell_root=CellSlice(reveal_dict_boc))

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]

    d = VmDict(64, cell_root=Cell(reveal_dict_boc))

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]


def test_vm_dict_not_signed():
    for my_key in [int("1" * 64, 2), 0, 179, 57, 228]:
        d = VmDict(64)
        assert d.is_empty() is True

        my_value = CellBuilder().store_uint(32, 32).begin_parse()

        my_hash = my_value.get_hash()
        d.set(my_key, my_value)

        key_stored, value_stored = d.get_minmax_key()
        assert key_stored == my_key
        assert value_stored.get_hash() == my_hash

        from_dict = d.lookup(my_key)
        assert from_dict.get_hash() == my_hash

    with pytest.raises(ValueError):
        d = VmDict(64)
        d.set(-1, CellBuilder().begin_parse())


def test_vm_dict_signed():
    for sign in [1, -1]:
        for my_key in [int("1" * 63, 2), 0, 179, 57, 228]:
            my_key = sign * my_key

            d = VmDict(64, True)
            assert d.is_empty() is True

            my_value = CellBuilder().store_uint(32, 32).begin_parse()

            my_hash = my_value.get_hash()
            d.set(my_key, my_value)

            key_stored, value_stored = d.get_minmax_key()
            assert key_stored == my_key
            assert value_stored.get_hash() == my_hash

            from_dict = d.lookup(my_key)
            assert from_dict.get_hash() == my_hash


def test_vm_dict_large():
    d = VmDict(257, True)

    cb = CellBuilder()
    main_cell = CellBuilder()
    cell = main_cell
    for i in range(100):
        cur_cell = CellBuilder()
        cur_cell.store_bitstring("1" * 1023)
        cell.store_ref(cur_cell.end_cell())
        cell = cur_cell

    main_cell = main_cell.end_cell()
    cb.store_ref(main_cell)
    cs = cb.begin_parse()

    for i in range(10000):
        d.set(i, cs)

    d.set(-1 * int("1" * 256, 2), cs)

    cc_val = d.lookup(-1 * int("1" * 256, 2))
    assert cc_val.get_hash() == cs.get_hash()


def test_vm_dict_set():
    d = VmDict(32)

    # set(self, key: int, value: CellSlice, mode: str = "set", key_len: int = 0, signed: bool = None)
    e = CellBuilder().begin_parse()

    # Large value for test
    cb = CellBuilder()
    main_cell = CellBuilder()
    cell = main_cell
    for i in range(100):
        cur_cell = CellBuilder()
        cur_cell.store_bitstring("1" * 1023)
        cell.store_ref(cur_cell.end_cell())
        cell = cur_cell

    main_cell = main_cell.end_cell()
    cb.store_ref(main_cell)
    cs = cb.begin_parse()

    d.set(0, e, mode="replace")

    # Will not set, because no value already
    with pytest.raises(RuntimeError):
        d.get_minmax_key()

    # Test set with mode=add
    d.set(0, e, mode="add")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    # Will not update because already have value
    d.set(0, cs, mode="add")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    d.set(0, cs, mode="replace")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == cs.get_hash()

    d.set(0, e, mode="set")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    # Force signed
    d.set(-123, cs, signed=True)

    assert d.lookup(4294967173).get_hash() == cs.get_hash()
    assert d.lookup(-123, signed=True).get_hash() == cs.get_hash()


def test_not_valid():
    with pytest.raises(AssertionError):
        d = VmDict(2)
        d.set(100, CellBuilder().begin_parse())


def test_empty():
    d = VmDict(32)
    assert d.is_empty() is True

    d = VmDict(32)
    d.set(0, CellBuilder().begin_parse())
    assert d.is_empty() is False

    d.lookup_delete(0)
    assert d.is_empty() is True


def test_get_cell():
    d = VmDict(64, cell_root=reveal_dict_boc)
    c = d.get_cell()

    assert isinstance(c, Cell)
    assert c.to_boc() == reveal_dict_boc


def test_lookup_nearest():
    d = VmDict(64)

    for i in range(100):
        d.set(i, CellBuilder().store_uint(i, 64).begin_parse())

    def _f(key, **kwargs):
        key, value = d.lookup_nearest_key(key, **kwargs)
        assert value.load_uint(64) == key
        return key

    for i in range(1, 99):
        assert _f(i) == i + 1
        assert _f(i, fetch_next=False) == i - 1

    with pytest.raises(RuntimeError):
        # Can't load prev value
        _f(0, fetch_next=False)

    with pytest.raises(RuntimeError):
        # Can't load next value
        _f(100)

    d = VmDict(64, signed=True)
    d.set(8, CellBuilder().begin_parse())
    d.set(6, CellBuilder().begin_parse())
    d.set(-1, CellBuilder().begin_parse())
    d.set(-2, CellBuilder().begin_parse())
    d.set(-3, CellBuilder().begin_parse())

    assert d.lookup_nearest_key(6)[0] == 8
    assert d.lookup_nearest_key(-3)[0] == -2
    assert d.lookup_nearest_key(-1, False)[0] == -2
    assert d.lookup_nearest_key(6, False)[0] == -1

    # TODO: tests on invert_first


def test_get_minmax():
    d = VmDict(64, signed=True)
    d.set(8, CellBuilder().begin_parse())
    d.set(6, CellBuilder().begin_parse())
    d.set(-1, CellBuilder().begin_parse())
    d.set(-2, CellBuilder().begin_parse())
    d.set(-3, CellBuilder().begin_parse())

    assert d.get_minmax_key()[0] == 8 and isinstance(d.get_minmax_key()[1], CellSlice)
    assert d.get_minmax_key(invert_first=False)[0] == -1 and isinstance(d.get_minmax_key(invert_first=False)[1],
                                                                        CellSlice)
    assert d.get_minmax_key(False)[0] == -3 and isinstance(d.get_minmax_key(False)[1], CellSlice)
    assert d.get_minmax_key(False, False)[0] == 6 and isinstance(d.get_minmax_key(False, False)[1], CellSlice)


def test_set_ref():
    d = VmDict(64)

    for i in range(1000):
        d.set_ref(i, CellBuilder().store_uint(i, 64).end_cell())

    for i in range(1000):
        c = d.lookup_ref(i)
        assert isinstance(c, Cell)
        assert c.begin_parse().load_uint(64) == i

    d = VmDict(64, True)

    for i in range(-1000, 1000):
        d.set_ref(i, CellBuilder().store_int(i, 64).end_cell())

    for i in range(-1000, 1000):
        c = d.lookup_ref(i)
        assert isinstance(c, Cell)
        assert c.begin_parse().load_int(64) == i


def test_set_builder():
    d = VmDict(64)

    for i in range(1000):
        d.set_builder(i, CellBuilder().store_uint(i, 64) \
                      .store_ref(CellBuilder().store_uint(i, 64).end_cell()))

    for i in range(1000):
        c = d.lookup(i)
        assert isinstance(c, CellSlice)
        assert c.load_uint(64) == i
        assert c.refs == 1

    d = VmDict(64, True)

    for i in range(-1000, 1000):
        d.set_builder(i, CellBuilder().store_int(i, 64) \
                      .store_ref(CellBuilder().store_int(i, 64).end_cell()))

    for i in range(-1000, 1000):
        c = d.lookup(i)
        assert isinstance(c, CellSlice)
        assert c.load_int(64) == i
        assert c.refs == 1


def test_lookup_delete():
    d = VmDict(64)

    for i in range(5000):
        d.set_builder(i, CellBuilder().store_uint(i, 64))

    total = 0
    for _ in d:
        total += 1

    assert total == 5000

    for i in range(4999):
        cs = d.lookup_delete(i)
        assert cs.load_uint(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 1

    d = VmDict(64, True)

    for i in range(-5000, 5000):
        d.set_builder(i, CellBuilder().store_int(i, 64))

    total = 0
    for _ in d:
        total += 1

    assert total == 10000

    for i in range(-4999, 4999):
        cs = d.lookup_delete(i)
        assert cs.load_int(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 2


def test_lookup_ref():
    d = VmDict(64)

    for i in range(5000):
        d.set_ref(i, CellBuilder().store_uint(i, 64).end_cell())

    total = 0
    for _ in d:
        total += 1

    assert total == 5000

    for i in range(5000):
        c = d.lookup_ref(i).begin_parse()
        assert c.load_uint(64) == i

    for i in range(4999):
        cs = d.lookup_delete_ref(i).begin_parse()
        assert cs.load_uint(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 1

    d = VmDict(64, True)

    for i in range(-5000, 5000):
        d.set_ref(i, CellBuilder().store_int(i, 64).end_cell())

    total = 0
    for _ in d:
        total += 1

    assert total == 10000

    for i in range(-5000, 5000):
        cs = d.lookup_ref(i).begin_parse()
        assert cs.load_int(64) == i

    for i in range(-4999, 4999):
        cs = d.lookup_delete_ref(i).begin_parse()
        assert cs.load_int(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 2


def test_set_get_item():
    d = VmDict(256)

    test_builder = CellBuilder().store_uint(0, 64).store_ref(CellBuilder().store_uint(1, 64).end_cell())
    d[1] = test_builder
    d["test"] = test_builder
    d["oh my god"] = CellBuilder().begin_parse()
    d["test2"] = test_builder.end_cell()

    cs = d[1]
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1

    cs = d["test"]
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1

    cs = d["oh my god"]
    assert cs.bits == 0
    assert cs.refs == 0

    cs = d["test2"].load_ref(as_cs=True)
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1


def test_large_key_map():
    cs = CellSlice(config_44)
    cs.skip_bits(8 + 1)
    suspended_until = cs.load_uint(32)

    d = VmDict(288, False, cell_root=cs.load_ref())
    blocked_addresses = []

    def load_key_value(key: CellSlice, value: CellSlice):
        wc = key.load_int(32)
        address = hex(key.load_uint(256))[2:].upper().zfill(64)
        blocked_addresses.append(f"{wc}:{address}")

        return True

    d.map(load_key_value)
    assert blocked_addresses == ['0:0000000000000000000000000000000000000000000000000000000000000000',
                                 '0:00ED1C8D25C4774E0EF3FC1C176FCD5E3C3BEB2F2B506A73BAD9303AEA648313',
                                 '0:0769FFDEA3D8261CB8844691F963979BAFFCF8A57E0DCAC0263CC7076BD4976A',
                                 '0:08082A325D5E0D291EB4487C38182D0DB474853A9846C36B5171B545F2F41EAB',
                                 '0:0927AFD84711FEA63794C619DED2288C7479B3EC16C927F0360ED76603F6DF06',
                                 '0:0CCB694F7476543E6EBDE59F9B87467575CB5AE315D7EDF97A7657364973A588',
                                 '0:0D5F5B9128665FC8F23011A217AD1D193AA69D72DE6AD7476F2B1588C71ED242',
                                 '0:0FEC8CF9CEFCE0E363A6AE3BE7D8A0060A46F91FAB5806D8FAA7E1AC6C8A4C29',
                                 '0:14CC4F8D79FF343BD74B672F751DF3E239BE84110F18AB258AC8853E29E6982C',
                                 '0:150F71678BD23A8FC5DE48897EC00181121AA16A67BA3AD018D0649C293D03F5',
                                 '0:186ED0C264419100E5DA07A5B056A173613775CD9832A75E4122ECBD9F4DBD93',
                                 '0:19A67FDECA75657FB222D9DEA33FFA755113EB745F45DD2EC38AE750C9E9648F',
                                 '0:1A242B8250D00DC0B76FA953688AF6B553D1478465C55030C5835C17EE8192F6',
                                 '0:1B98C2FDDF1BD44FE8810C9ACE7E1891192B37BCE733132F432406EE09BEDA53',
                                 '0:1C7C0347ECF1B679E4DD5F956BD9951E6F109FC09CB3042138A2B8945515378C',
                                 '0:200144A57FDCE64376E61DEB7995BEA7F61D490B42121793CC1FBA2B67CBFB95',
                                 '0:202B511CAEF12E2FDB02B688F770D85534EB9FDE5A391883C4DA09F57F065960',
                                 '0:22530A45DBBBD70A782A3617FF4D0E44FF4E9A8741B8CEE4AB9DF53B08B2DA86',
                                 '0:22E69F616AECAB212A3AA133F596FB4345CA51FBC0D755FC05A0BB525C2CD42B',
                                 '0:23B513F5915F0D4B6A28E8DEBB1B5C0638E58C309772CAEDF55A838A70A625DC',
                                 '0:23B5EEEA91290C0D32305F4CEA83644899B504DA1061AF6EEEC86B284882995C',
                                 '0:24BD5413B4F996618EB848B23E0CA4BAA016D043426B18EC8B87DDCD9AB60F41',
                                 '0:2D94745933217EF0F1D1C92BB95627B40B657F4616794756F90B8B6F9D3B62EA',
                                 '0:2EA405FA4CC0019C9BA47FF5CF5CD8A1FD3D59800063A31B4070E3DC03BD7421',
                                 '0:2F092C8B0A8DB51ABA8B0227DDA2FE1690EC6E1900A3311C6017571749A3732C',
                                 '0:2FFFF28B9B9D19CFD88DEA7D81176786B41ECAC237DED40832DE592377D15226',
                                 '0:312F4A05D7ECCD82298F2AD85B0E7612E318FDE2B1ED7CD44DEFF3DDD6BD8B34',
                                 '0:3227AE037FB55F6FCFE39A51A7B19072180742B04580FC57D65F254453977A0A',
                                 '0:336FD10FD51007C7C639D84494716FAC6D19EB6AA0ED4E823B2DCC2FF73A4E35',
                                 '0:3457022D52A7209684AC3A8E633819F4926B59DFC0D889D350E12151F63354F6',
                                 '0:34DE8FB422016BB981681E8B7DE82FF01FDA402AB5591900443561D561F37C77',
                                 '0:396EFC56779FAADAF25456A47D0256C421F745CAC2D1D0F5C68159417FCC7985',
                                 '0:3CFD6E07318CAC5199F32B2440BA05B1D3090F96357A82DC7FB3E7DD60670D00',
                                 '0:4196B680A6CD0E65A07D43C78F427DB054068BD46E35D40F9D369A7259EDD7DC',
                                 '0:42D8CDC3975887F2907A920EDDE6F761DA733FD7468583E45E32CB4010FC4D28',
                                 '0:4304A139586288967A22DCE3B3C3BBE428A217E797968CFBE0C495B07A4F00C8',
                                 '0:495256F32BB4932BA478D8B7061712EBB9D2B132E5B9829AC6001726483843A1',
                                 '0:52CDC190DDBEEB86CCEC2D25A4759900A1F46D45EF45B78962D0E506928EA39E',
                                 '0:52F54DC07C3D797C698EB51317400C5C3D507036E22D7CB7039E2F5F91B4F2C8',
                                 '0:567CCAEF29948438793CBFFFA4B1EAC1A62276ADECCA6EE12160B7D91AA897E9',
                                 '0:57D433AF4A8C768E78CDE34645B5449085224C0B211684145D4444514A5B626C',
                                 '0:5938393F375DA0A562274E94542C69350B8B3F7309032FDDAD7255D0CAF022CF',
                                 '0:59FFCA801CA64D630735FD09534E1B2F31F525A9E6DA07083554CBC738B8F486',
                                 '0:5ADBDEF467512619FFB747E061EEDDD699130716B601F89771679162A1352B7C',
                                 '0:5B8EB5C7A310F2875658181741A1080B6927315BAA594758448490BC06A17EE4',
                                 '0:5C2744ACC49F1589842BD27D5E29890D7CACCD08ED5442ED1C85D0B7B02F4232',
                                 '0:5D0AF141E1B03B3C03F45579D3B3BF384CEFF80A858B6F542A45DCABD28ACB02',
                                 '0:5D7E73F319B6CADFC7941D46F530764276B8AD58331B123F9F8CF7518AF76BB8',
                                 '0:5F3FA1E81DBFF3A9CE54DCB87CFE934CB7447B230B31BBCE7C77476A99E01187',
                                 '0:5FE31152CBE3045DCC14B6AD5B0FF14A0D6CD22C9E2DE601E160ABAC3352D5C1',
                                 '0:606EEC7B5528EA2473FB07244AD6AE10B9565BA5209EB0D82FCF9A9A77795F5D',
                                 '0:60B8C4878C5BF96DFA0E76C86BDEBB92F7299267385128CA2FA0DAF11B1657BE',
                                 '0:62012A94A9A562CEBA332D16ECCE4582DA41136E48693B6AA78835433CF836FF',
                                 '0:6230D2FDA8D58C024247B8CD0116779872E1CBD7B9334B8A6CC296843BE3465A',
                                 '0:62B5D143A14E435928DF2AAEC0B0EDBD448C009C1CF3BDC5554A7E5E910A01F4',
                                 '0:63F102C5D902D4D0A0CC09576EE7AF3342C85BA6D5A5357DBCA0785305B985FD',
                                 '0:6677FA11F3C4EB7C019C2AB327E384F7C019DB8774D65505ABF2B56AD1B6139D',
                                 '0:676963A7C0DFE6A9C0C41776910CBBCB3CB855DFFBADB99AD7DC88CB74761E0B',
                                 '0:68EE815E7DF6641338DC9B6A3DC9DB1F6A773A1616C0E6E75DC0665CBECB4598',
                                 '0:6A035CA23B47C3E1A5CCB24E214013B8AD67F3C7674DA63DD4D6C763DB51B2E8',
                                 '0:6A8958E685EDA25469A03920CED451A34A2CFF00CB5BD70EE52C488FE17205FD',
                                 '0:6C0A12DF8596DA476DE025A47C49EBC85E8C1EDAE52D2100B38EE72E03D8AEDF',
                                 '0:6C9CCE64FEC3B39D0AF559D13DE077C258349E2CAE9C0588B9C51C40A74917A0',
                                 '0:6D4ACD125383C243C1F8ABC42AA0AD0B3F024B91C272C0BCFD5A09195E5FD3EB',
                                 '0:6ED90D443BC808A0D035AA81969C752E74A7E6AA52840D3404F83C4DFBFE2C76',
                                 '0:6FFB4CEC37D8FE2F1B3512F6C61B47CCC1B79EA9B5A5C53CF28D5E0B13ED2E25',
                                 '0:7077DD1DD31DBAB37C0E74E602570FB3DA06D1EE140998243C53BCFC569E632C',
                                 '0:72E1297457AF8EB3CFE76E05132F891CC38B0671413AAF5D78E8485096AE23D2',
                                 '0:756953321418679585E6423B266B44BADE4BF1294EDC719285342153C17EC048',
                                 '0:759B6CF34CB71967300EC403107761B1D01F960512C45F05F2537314A6BB9944',
                                 '0:77FB08067D071BA69A3E5E75ECBF3C2BEF21E08501F4EE9E9F302FC045D2228F',
                                 '0:78873BE25710F5EF480865FB163C614A7DB381E8B08FE58847EC8EDF5B3EF077',
                                 '0:78E7B2F646EEDE090F0D8604ADA07C6F7B0552B0A08386AC9370BE3BC509D669',
                                 '0:7BB000BE851906824DB0DD13019427CD930E954C2E836BE191995B17287E0859',
                                 '0:7BD6ACE07A1217A0C463E7CBC059A1E73408BA517114E427BDE36749A9FE076B',
                                 '0:8133202279E99FDEF177BA6634942690C4B870BDB4C5B8BF1E4313D8AE9799F0',
                                 '0:81797AADEC88B02287D9FAB623CFA8127912E31632DD1507FFB91AD79D96AE2B',
                                 '0:820891E001CB3EC10CE07FFF483CA7649F0FDE8F467E43E9F706D4842A2D2122',
                                 '0:832AA2F9C3FE8C0FE67B00E06EB6EFAE47E6494EC80D5357EEE3AE219FD82B63',
                                 '0:853A00DE1B6B5BFF13112794D00D8ABA04F9484A6F4A4B13A3BC6C0DDF6989FB',
                                 '0:85DD813ECE0B0250A34338EF881DC2A068DB836E16D3DA63C3A7A084A00FE51B',
                                 '0:8670DE1BD64DBE4CEADF00C3A46B7471BE5C1C7150D22B470F7B39476607CBC7',
                                 '0:871D8551BD6EC4AAD0598ED786AEFCEB6ECDA5899880254C9EBD1399676855DF',
                                 '0:873879B429A6462EA0CF51944774B6103BE9EC1C7ACB6849AB7D0F7985DF0C53',
                                 '0:8824B345224A390AFA4A9FDA0092B0E02E87033A80F8BF0987C4DC7F7EC1BF2E',
                                 '0:8A828F7338A2077843E6FC1C9206C0E2EB5BC912CC37E9E61D49F12401D109C5',
                                 '0:8FA7DA857B09B99185819CEED2E20978FF2F8D3EE19973BE59849D93F1CAE42B',
                                 '0:9257D26E1AA4C5BF1840F1B6777ECF4BA0EF9BE81DDF8E89B4906C0DBEB543E2',
                                 '0:9343C90FC325FDDABE3C80220BFE92CDFD17104FD8216728279834D890E92E5B',
                                 '0:9376F0C27F46C0E5D38F235FB8E2D07665F35C3068A4973BE0DBB4E8BE00C4A8',
                                 '0:93AC54521EDFAD7E4ED6C4AF591D09AA2DC8315F14CAEF019F0846EA818D96F4',
                                 '0:952FE93A75E0D1E7A67CA5C6F406D8349467DA8AF3867DD0C20F5BEFC91B322F',
                                 '0:973696D592E2B14F13DB7381969E04ABAC18E1443D134125EAC695BF83E5A10A',
                                 '0:9A4821D56A4FA321CF4036EB5301F1E964D33761D1A4CBBC9A0F3B13AE0D1684',
                                 '0:9EE0060805C7B5A40936A8924F4ACD4ECF265194A8E47EAF33B82F03EDEAEFE8',
                                 '0:9EF583316539952B7D1B689C24338C3485CEB46FE25FFDE1316CF688BE450EA4',
                                 '0:A3CED23F38B77551326D498DE8FDBF2A6710F9B131687891C803F09F43716B8A',
                                 '0:A94E11BD39F607A7BEF279A512FFDE668473D582ABDEAC83B9D1138DCACC1602',
                                 '0:AC2E90DE1C1DAAA516E6B026FFD319AC615371D4D81E62BBC7193D530EB1E40E',
                                 '0:ADAED4D7100A12A681119A2A8E9C809EF4B1F19F637CF4DE011FDA9D1E5AC6F9',
                                 '0:AEB44A5B2896AE95EBCE61740FAA59A088C8070D4E82E97ECA471A45CB33DFD1',
                                 '0:AFDBCCB8F4675A2E7728725BF421274394C518FDCC433C63561423D3F2DE06BA',
                                 '0:B42664F2A6AC921D531524C1D6B296F7C6BB362EB772E1E27E33B431A5B4B870',
                                 '0:B50E6FC3BEE08644516AAD9D1190F09A4C90C06872967293F768DDDFFD3189D5',
                                 '0:B81B6A61E804BF983FFE708BF8688626D73E63020096FD34C312BEF6CA05CE3F',
                                 '0:B9416647545B2735CDD83D161A7D412B160FE2D2C970A128B24E88C177AD536A',
                                 '0:BA002AB75403598EA7D1072EC93079292F0A90F6AC9826C0881B1D6661B420C5',
                                 '0:BAA3C50DDB54CBBEDEA3EC6E2E892D4F0772C1F0EFCC77BD199A4F6E89C4633E',
                                 '0:BB6C62EA2365CF74A189CCD9643E73A7077624C34410F6520C642656E465AFA6',
                                 '0:BE41E675DD03F496CCF134AB77F347C25AE695F78BF00BF6DFBAA9AB960D7F7C',
                                 '0:C283DDE5515C66942124B3990BF234C572A83C94495F022F1D49E7BC8F68C50C',
                                 '0:C4D070607E43A2A877B32ED1310464EF3ACF1E8ADB611D0A2C0635B70660F2D7',
                                 '0:C4F7C5CDCD788FABB5676C9276338F87B77B57FCE591D315134E70C2F0D39B2E',
                                 '0:C705422111D502509D7DF7AF92123D168AB69A13827A60B24EB8B28BA4AF2E81',
                                 '0:CB3503B1117458E8908BA71424A078EC648BE57C1706C6685DA71731C3B85DD3',
                                 '0:CCB433303A8B52528C2967CDCD7E9609602FD762F408A8161CB83509A0571E7A',
                                 '0:CE811136B1B98F66997D940E98DE2C523C50FC085FEBA4B97A37D9FA8B42A12F',
                                 '0:CEB453ADE35B246E3064645F3DA185E9A031028E5C48CC3F9285600E632CEEC6',
                                 '0:D23141B0B76E4841DDFFC878C8D3717BD46F0AA7618C68C12FD93896A1329BB3',
                                 '0:D3DF81835A2722628EB6B846E84BCB23DE194A51701661C33752B73436308C83',
                                 '0:D6B4F659805EF0BC83141D94288EE0F7BAD8AE8AFB16ED6B25449DF7760BFEE7',
                                 '0:D6B6FF8B69FCD0ADBD4E22959C0CA1E8ED8BEDD96A508AD94CDB7FB6924B0CAE',
                                 '0:D8E4683041EB92670047EF67B439008F41EAEA02C6513D1C7A0954F139BD8DFB',
                                 '0:DC07E998D553B4563B020DEE62D3E9D38298B2C22BB852E980CC7E687354A293',
                                 '0:DF7910C4D530E1C2DE3BF020D1D10ECC0F0A9C4D485F8EAC934F9F6682801A17',
                                 '0:E28DC13250A6BE42009B786960810935B81B6DD99447C96E18E2007847A30DE9',
                                 '0:E2B0177C53B337084399F2071609D7AD766262DC0237D73213E6A07039D9946E',
                                 '0:E6C2F68AD9DFD26DA3DDA4E33AD1E7DF3D678AB24B200D5C053C4CB1B9FB4CDF',
                                 '0:E8CE75FA386A1DAF00A489851EB7441084AA83E6FB3F5D5A16930F4F588ADCE2',
                                 '0:EB0635B137F6667B96AE4459F9A8A359B687FAAE59307920867FD8B3EB42661A',
                                 '0:EB662DFA2A319C3BEE59FBA009F40A76BE064A7FB27370C47811D8C4E5FEEA95',
                                 '0:ECCF124F399017D33B6695BB3B78380F970AF7B6B9BCFA7CC57C07666CA86E81',
                                 '0:ECEB82522275740372BF32A3DA6FBA83D8C68990D04AAB9B71C774507B9126C9',
                                 '0:F01AEE2F16FD5EDF09FC9A29FF8B2ECE3C95DE80E613150E5B6456796B964F88',
                                 '0:F1921990BCF0ED81C36CB7BE49C97ADEE85D5DF4703946B4247C09BEE8461B79',
                                 '0:F1DAF90B511A49638C5EA18E2304D23ECB9E73232640E1EA66016A1BF74A0B9F',
                                 '0:F24F7EB392D04DF4F556BD9D63A11C6121F1148023EDE05DA2B1AF9E9D403F77',
                                 '0:FAB767570E36711750EABA7285FBC7445A2BC9765898FF41588825E7B61BAA9C',
                                 '0:FE9E1AE29E3BF40782D382BD1D4474C7C07D4C3AC80684A05725977BBC448C65',
                                 '-1:01B573BD6DC4CC5E383D6E08AF2A1E258499995903CFEBFADBF6F7E39533F914',
                                 '-1:02A28D6B20A24A05477CFCEA76C7D3E7EAA2A9CCAF21897477EA990039BB25B2',
                                 '-1:062BB40F112FFAAC45F54209C9A187DC95F9A6C4B07B264664832323398E2299',
                                 '-1:19BD614293AE2E6DD4FB93D7C00E50000D95B6A14784D05FFF84D031E6F990DB',
                                 '-1:28E8033DB1467CACEA8B158F0F61E682DE06E8A5947504C904F1F703D2BE4D9E',
                                 '-1:2C3062B2A70D34E8079162A8A62E3998D947E9F921E4F02D19241360541973C3',
                                 '-1:3414D2793493B8FB44309550167245195DD93E3DF6037B10D9D7E8EEF52C6117',
                                 '-1:35F14297CDE39E6F3E927F4FEB76AED94A084F57E8ABE21C5455F34DA008F7B9',
                                 '-1:3DC61FAECBCEB4FA609CBD2F3370052CF1B0299B12C6CA00CB10A8D493944BFB',
                                 '-1:3EB1651EFAAF65221A9B43CB849FDCEAD2C8B6758C2654D93BB80825988CEFE8',
                                 '-1:4BCA71C72A007163AFA5F96FDD58DF82B464F6FE38B9ACDDC4CCE23EA7DCD611',
                                 '-1:4E2B4087AA806275C114247C789DA5774ED82652FD681211A9B770C52C69E772',
                                 '-1:50CEEBAB9D128691D06488571531A858D0D783CBD44848B2E62CA6099E9D03F5',
                                 '-1:5EC36A53DC55D2FA6F304479DE7F54A9877F03BF637AF7F492583AB52FB73DF1',
                                 '-1:6131DEFC8334A256C2B4CF3D001ED1236BCC7552807F34364C8E7FA5F3A3502B',
                                 '-1:660ECAB3220DA2F1F770D016FB50669F03719CD6A5F92188E9E80399C0695FBE',
                                 '-1:6680F4D15366A1C672AD2F0B3EEA20770260630F70582ED008A6A27275A8B3B2',
                                 '-1:66D44782557077D989B3883AA7499BE3933CDE99D73D1BCA42AED3D529FB173F',
                                 '-1:67CE3E9105CE2643AA779E0EE6189EEDA7B31BCC44617BBA1B90CF40D309C208',
                                 '-1:6B53EFC00270641C1EF54C80B742F51FE4B700B2F8F40782286330172E910577',
                                 '-1:707CF9EFF139C9E7F83DF22FC4869047FF497031DE94521FF2DFDD40C2EB3C46',
                                 '-1:8A49896DD0A389EAF292A3573CDFB37FF4B89C4C9965D8C83B1DB8B1EDBB2F20',
                                 '-1:8CA766A670559CFD65192E9EEED29C7EC5A1544C8BD9DB7E5B6E4C5E663FF42F',
                                 '-1:8E9735C300C1A005649A19B0A1DDE75D38C2904351714A695CED416FCA0D052E',
                                 '-1:8EA7CE472073D6DFC6D11BE7084D384DB4DEC32CC3CD5EE39CB6194BC16210E0',
                                 '-1:9635D332838598E3BED341B7115D74586894F14DCB0C5C21426AA36C24EC766D',
                                 '-1:9DD3BFB670C27F144544555C803057B8F5A06E467871CC50B1AFBD7CF65F82DB',
                                 '-1:A83D524CE9F18FF4E0BE3DCCCC51D88A3CD7F0914AEDE1EB258335D7118D2A08',
                                 '-1:B17045F9F82DB60C4F3A4BB1206E108DEF01A2E2B400DF969771A7E3392555AD',
                                 '-1:CE5F3FE4B464C70A56FC6ABCCBB775C48E5253C3D2C46318C6BD224D7DFEFD96',
                                 '-1:D0D9B5213A7E0C03A3873C58BFE9B9A60F2AB17CD3DED31675373B958378999D',
                                 '-1:D28D64B320B0A0530AB88A00C3104DEFDD27F4034CF03B9E5A584F8B6332C6A4',
                                 '-1:DAE40EE38DE9A0F542319BCA8A0C90CEE84C75CB4A8860A1EFD72E89576A5FD0',
                                 '-1:DAEC5B9B51F23C7D43E700866F21129A742F461BACE98CB2C4E8F5D58FE75EE6',
                                 '-1:DF7486D3868A0FB38FEBD8313F67A66C5B27097472E7B2E2802474DC6DA65A8A',
                                 '-1:DFBEB774841A15254C688BBC07D7BDD993C34F8B256FC61E48A184A311865B3A',
                                 '-1:E5BDAD2A1226615ABAD9265F88271C82713426993A3BD5F216C90DF51F127C36',
                                 '-1:E69571E7B9F58EDFEBEFA297E547F36920532289DBE9FF1B76D107FCBAC30104',
                                 '-1:ED2CBA0B988BDAA12C4A5F5B177E51D93B54C7CD2F91515214BB1FA04FAEF290',
                                 '-1:EF03AC917E6B763F85079F196B4146457019CABB1F262F678CA8182978C14FA2',
                                 '-1:FC3D252D2B2FD4F8964348D50DA8DE5C56C9FD39126A4BDDCBE8344CF476ECA1']
