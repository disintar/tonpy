from tonpy.libs.python_ton import PyStackEntry, PyStack
from tonpy.types import Cell, CellSlice, CellBuilder
from typing import Union
from enum import Enum


class StackEntry:
    class Type(Enum):
        t_null = 0
        t_int = 1
        t_cell = 2
        t_builder = 3
        t_slice = 4
        t_vmcont = 5
        t_tuple = 6
        t_stack = 7
        t_string = 8
        t_bytes = 9
        t_bitstring = 10
        t_box = 11
        t_atom = 12
        t_object = 13

    def __init__(self, value: Union[Union[Union[Union[None, Cell], CellSlice], int], CellBuilder] = None,
                 entry=None):
        if entry:
            self.entry = entry
            return

        if value == None:
            self.entry = PyStackEntry()
        elif isinstance(value, int):
            self.entry = PyStackEntry(big_int=str(value))
        elif isinstance(value, Cell):
            self.entry = PyStackEntry(cell=value.cell)
        elif isinstance(value, CellBuilder):
            cs = value.end_cell().begin_parse(True)
            self.entry = PyStackEntry(cell_builder=cs)
        elif isinstance(value, CellSlice):
            self.entry = PyStackEntry(cell_slice=value.cell_slice)

    def get_type(self):
        return StackEntry.Type(self.entry.type())

    def as_cell(self):
        return self.entry.as_cell()

    def as_cell_slice(self):
        return self.entry.as_cell_slice()

    def as_int(self):
        return self.entry.as_int()

    def get(self):
        if self.get_type() is StackEntry.Type.t_null:
            return None
        elif self.get_type() is StackEntry.Type.t_cell:
            return Cell(self.as_cell())
        elif self.get_type() is StackEntry.Type.t_slice:
            return CellSlice(self.as_cell_slice())
        elif self.get_type() is StackEntry.Type.t_int:
            return int(self.as_int())


class Stack:
    def __init__(self, prev_stack=None):
        if prev_stack is None:
            self.stack = PyStack()
        else:
            self.stack = prev_stack

    def __len__(self):
        return self.stack.depth()

    def __getitem__(self, item) -> StackEntry:
        assert isinstance(item, int)
        assert item <= len(self)
        return StackEntry(entry=self.stack.at(item))

    def pop(self) -> StackEntry:
        return StackEntry(entry=self.stack.pop())
