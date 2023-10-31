# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PyStackEntry, PyStack, make_tuple, deserialize_stack_entry, deserialize_stack, \
    PyContinuation
from tonpy.types import Cell, CellSlice, CellBuilder
from typing import Union, Iterable, List
from enum import Enum


class Continuation:
    def __init__(self, cont: Union[CellSlice, PyContinuation]):
        if isinstance(cont, PyContinuation):
            self.cont = cont
        else:
            self.cont = PyContinuation(cont)

    def type(self) -> str:
        return self.cont.type()

    def serialize(self) -> Cell:
        return Cell(self.cont.serialize())


class StackEntry:
    class Type(Enum):
        """Possible types of StackEntry"""
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

    def __init__(self, value: "None | Cell | CellSlice | int | CellBuilder | list | Continuation" = None,
                 entry=None):
        if entry:
            self.entry = entry
            return

        if value is None:
            self.entry = PyStackEntry()
        elif isinstance(value, int):
            self.entry = PyStackEntry(big_int=str(value))
        elif isinstance(value, Cell):
            self.entry = PyStackEntry(cell=value.cell)
        elif isinstance(value, CellBuilder):
            cs = value.end_cell().begin_parse(True)
            self.entry = PyStackEntry(cell_builder=cs.cell_slice)
        elif isinstance(value, CellSlice):
            self.entry = PyStackEntry(cell_slice=value.cell_slice)
        elif isinstance(value, list):
            self.entry = StackEntry.create_tuple(value).entry
        elif isinstance(value, Continuation):
            self.entry = PyStackEntry(continuation=value)
        else:
            raise ValueError(f"Type {type(value)} is not supported")

    def get_type(self):
        """Get type of stack entry"""
        return StackEntry.Type(self.entry.type())

    def as_cell(self):
        return Cell(self.entry.as_cell())

    def as_cell_slice(self):
        return CellSlice(self.entry.as_cell_slice())

    def as_int(self):
        return int(self.entry.as_int())

    def as_cont(self):
        return Continuation(self.entry.as_cont())

    def as_str(self):
        return str(self.entry.as_string())

    def as_tuple(self) -> List["StackEntry"]:
        return list(map(lambda x: StackEntry(entry=x), self.entry.as_tuple()))

    def as_cell_builder(self):
        return CellBuilder(self.entry.as_cell_builder())

    def serialize(self, short_ints=True, continuations=True) -> Cell:
        mode = 0
        if short_ints is False:
            mode += 1

        if continuations is False:
            mode += 2

        # mode: +1 = disable short ints, +2 = disable continuations
        return Cell(self.entry.serialize(mode))

    @staticmethod
    def create_tuple(items: Iterable) -> PyStackEntry:
        def __convert(value):
            if isinstance(value, StackEntry):
                return value.entry
            else:
                return StackEntry(value=value).entry

        return StackEntry(entry=make_tuple(list(map(__convert, items))))

    def get(self):
        """Convert stack entry to type"""

        t = self.get_type()

        if t is StackEntry.Type.t_null:
            return None
        elif t is StackEntry.Type.t_cell:
            return self.as_cell()
        elif t is StackEntry.Type.t_slice:
            return self.as_cell_slice()
        elif t is StackEntry.Type.t_int:
            return self.as_int()
        elif t is StackEntry.Type.t_builder:
            return self.as_cell_builder()
        elif t is StackEntry.Type.t_tuple:
            return self.as_tuple()
        elif t is StackEntry.Type.t_vmcont:
            return self.as_cont()
        elif t is StackEntry.Type.t_string:
            return self.as_str()
        else:
            raise ValueError(f"Not supported {t}")

    @staticmethod
    def rec_get(value):
        if isinstance(value, list):
            out = []

            for item in value:
                out.append(StackEntry.rec_get(item))
            return out
        elif isinstance(value, StackEntry):
            return StackEntry.rec_get(value.get())
        else:
            return value

    @staticmethod
    def deserialize(value: CellSlice) -> "StackEntry":
        return StackEntry(entry=deserialize_stack_entry(value.cell_slice))


class Stack:
    def __init__(self, values_list: Iterable = None, prev_stack: PyStack = None):
        """List of StackEntry"""
        if prev_stack is None:
            self.stack = PyStack()
        else:
            self.stack = prev_stack

        if values_list is not None:
            for item in reversed(values_list):
                self.append(item)

    def __len__(self):
        return self.stack.depth()

    def __getitem__(self, item) -> StackEntry:
        assert isinstance(item, int)
        assert item <= len(self)
        return StackEntry(entry=self.stack.at(item))

    def __iter__(self):
        total = len(self)

        while total > 0:
            total -= 1
            yield self[total]

    def __reversed__(self):
        total = len(self)
        cur = 0
        while cur != total:
            yield self[cur]
            cur += 1

    def append(self, value: Union[Union[Union[Union[Union[None, Cell], CellSlice], int], StackEntry], CellBuilder]):
        if isinstance(value, StackEntry):
            self.stack.push(value.entry)
        else:
            se = StackEntry(value=value)
            self.stack.push(se.entry)

    def serialize(self, eoln=False, lisp_stype=False, serialized_bocs=False) -> Cell:
        mode = 0
        if eoln:
            mode += 1

        if lisp_stype:
            mode += 2

        if serialized_bocs:
            mode += 4

        # mode: +1 = add eoln, +2 = Lisp-style lists, +4 = serialized bocs
        return Cell(self.stack.serialize(mode))

    def pop(self) -> StackEntry:
        return StackEntry(entry=self.stack.pop())

    @staticmethod
    def deserialize(value: CellSlice) -> "Stack":
        return Stack(prev_stack=deserialize_stack(value.cell_slice))

    def unpack_rec(self):
        return StackEntry.rec_get([i.get() for i in self])
