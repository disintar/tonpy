from tonpy.types.stack import StackEntry, Stack
from tonpy.types import Cell, CellSlice, CellBuilder


def test_stack_none():
    t = StackEntry()
    assert t.get_type() is StackEntry.Type.t_null


def test_stack_int():
    t = StackEntry(32123121231)
    assert t.get_type() is StackEntry.Type.t_int

    tt = t.get()
    assert isinstance(tt, int)
    assert tt == 32123121231


def test_stack_cell():
    t = StackEntry(Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp"))
    assert t.get_type() is StackEntry.Type.t_cell

    tt = t.get()
    assert isinstance(tt, Cell)
    assert tt.get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'


def test_stack_cell_slice():
    t = StackEntry(CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp"))
    assert t.get_type() is StackEntry.Type.t_slice
    tt = t.get()
    assert isinstance(tt, CellSlice)
    assert tt.get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'


def test_stack_cell_builder():
    cb = CellBuilder().store_uint(10, 64)
    t = StackEntry(cb)
    assert t.get_type() is StackEntry.Type.t_builder
    tt = t.get()
    assert isinstance(tt, CellBuilder)
    assert tt.end_cell().begin_parse().load_uint(64) == 10


def test_stack_stack():
    cb = CellBuilder().store_uint(10, 64)
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    c = Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    se = StackEntry(11)

    s = Stack([10, cb, cs, c, se])
    assert len(s) == 5
    assert s[0].get() == 10
    assert s[1].get().end_cell().begin_parse().load_uint(64) == 10
    assert s[2].get().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert s[3].get().begin_parse().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert s[4].get() == 11


def test_serialize():
    cb = StackEntry(CellBuilder().store_uint(10, 64)).serialize()
    assert cb.get_hash() == '433877BA3DE8544BBA9DE329EECD324C4E934D5AF46A41C62C44D6F9C7AAEDE6'

    cs = StackEntry(CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")).serialize()
    assert cs.get_hash() == 'DB697A675BC36F7E6A97D9EBC8048F19C9C78B7BB904F196C4A066C7CBEC32E9'

    c = StackEntry(Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")).serialize()
    assert c.get_hash() == '0E418A8BD8268CAB20DD393465EEDF1775F4FE39C96B5B504B94177F9E9E7F0E'

    se = StackEntry(11).serialize()
    assert se.get_hash() == '3D45A4D59698AD7BECD4979361CFA7E84384E26099273239546A6B23ABE982C2'


def test_serialize_stack():
    cb = CellBuilder().store_uint(10, 64)
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    c = Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    se = StackEntry(11)

    s = Stack([10, cb, cs, c, se]).serialize()
    assert s.get_hash() == '78241E52B14D56C58495595AB665B207E6ED3CE6F889B1D8C16D88388EE30DDA'


def test_deserialize_stack():
    cb = CellBuilder().store_uint(10, 64)
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    c = Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    se = StackEntry(11)

    s = Stack([10, cb, cs, c, se]).serialize()
    assert s.get_hash() == '78241E52B14D56C58495595AB665B207E6ED3CE6F889B1D8C16D88388EE30DDA'

    ss = Stack.deserialize(s.begin_parse())
    assert ss[0].get() == 10
    assert ss[1].get().end_cell().begin_parse().get_hash() == \
           '2703D9A1D01AF9B0B0D7728C8A760C1DD0BC63C22BEB9E71AA3D07061343A54C'
    assert isinstance(ss[2].get(), CellSlice)
    assert ss[2].get().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert ss[3].get().begin_parse().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert ss[4].get() == 11


def test_deserialize_stack_entry():
    cb = StackEntry.deserialize(StackEntry(CellBuilder().store_uint(10, 64)).serialize().begin_parse())
    cs = StackEntry.deserialize(StackEntry(CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")).serialize().begin_parse())
    c = StackEntry.deserialize(StackEntry(Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")).serialize().begin_parse())
    se = StackEntry.deserialize(StackEntry(11).serialize().begin_parse())

    assert cb.get().end_cell().begin_parse().get_hash() == \
           '2703D9A1D01AF9B0B0D7728C8A760C1DD0BC63C22BEB9E71AA3D07061343A54C'
    assert isinstance(cs.get(), CellSlice)
    assert cs.get().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert c.get().begin_parse().get_hash() == '235CBBDDDA3C8397468C806412A211BD2672C6188D9728C62DD48B3DEED02BA6'
    assert se.get() == 11


def test_tuples():
    cb = CellBuilder().store_uint(10, 64)
    cs = CellSlice("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    c = Cell("te6ccuEBAQEABQAKAAVBX/xo8FXp")
    se = StackEntry(11)

    tp = StackEntry.create_tuple([10, cb, cs, c, se, [3, 4, 5]])
    assert tp.get_type() == StackEntry.Type.t_tuple
    assert tp.serialize().get_hash() == '8AFC0E4F34D520C7B36BFA4AD1704EF67BAD5ABB52C508CB9256816D07724239'
    assert len(tp.get()) == 6
