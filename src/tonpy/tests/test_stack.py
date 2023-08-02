from tonpy.types.stack import StackEntry
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
