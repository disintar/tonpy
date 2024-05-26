# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PyCell, parse_string_to_cell, load_as_cell_slice
from typing import Union

from tonpy.types.cellslice import CellSlice


class Cell:
    def __init__(self, pc: Union[PyCell, str] = None):
        """
        Cell is simple data structure of TON with up to 1023 bits and 4 refs to other cells  |br|

        :param pc: PyCell (c++) or BOC str
        """
        if pc is None:
            self.cell: PyCell = PyCell()
        elif isinstance(pc, str):
            self.cell: PyCell = parse_string_to_cell(pc)
        else:
            self.cell: PyCell = pc

    def to_boc(self) -> str:
        """Convert cell to BOC string"""

        return self.cell.to_boc()

    def get_hash(self) -> str:
        """Get cell hash"""

        return self.cell.get_hash()

    def get_depth(self) -> int:
        """Get cell depth"""

        return self.cell.get_depth()

    def begin_parse(self, allow_special=True) -> CellSlice:
        """Convert cell to CellSlice"""

        return CellSlice(load_as_cell_slice(self.cell, allow_special))

    def is_null(self) -> bool:
        """Some cells are nulls, you can't operate with such ones"""

        return self.cell.is_null()

    def dump(self):
        """Recursively dump all cells as hex"""

        return self.cell.dump()

    def dump_as_tlb(self, tlb: str) -> str:
        """Dump as C++ PrettyPrint parsed by TLB type"""

        return self.cell.dump_as_tlb(tlb)

    def copy(self) -> PyCell:
        """Copy current Cell"""

        return Cell(self.cell.copy())

    def __getstate__(self):
        return self.to_boc()

    def __setstate__(self, boc):
        self.cell: PyCell = parse_string_to_cell(boc)

    def __repr__(self):
        cs = self.begin_parse()
        b = cs.bits
        r = cs.refs
        del cs

        return f"<Cell [{b}] bits, [{r}] refs, [{self.get_hash()}] hash>"
