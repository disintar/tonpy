from tonpy.libs.python_ton import PyCell, parseStringToCell, load_as_cell_slice
from typing import Union

from tonpy.types.cellslice import CellSlice


class Cell:
    def __init__(self, pc: Union[PyCell, str] = None):
        """
        Cell is simple data structure of TON with up to 1023 bits and 4 refs to other cells

        :param pc: PyCell (c++) or BOC str
        """
        if pc is None:
            self.cell: PyCell = PyCell()
        elif isinstance(pc, str):
            self.cell: PyCell = parseStringToCell(pc)
        else:
            self.cell: PyCell = pc

    def to_boc(self) -> str:
        """Convert cell to BOC string"""

        return self.cell.to_boc()

    def get_hash(self) -> str:
        """Get cell hash"""

        return self.cell.get_hash()

    def begin_parse(self) -> CellSlice:
        """Convert cell to CellSlice"""

        return CellSlice(load_as_cell_slice(self.cell))

    def is_null(self) -> bool:
        """Some cells are nulls, you can't operate with such ones"""

        return self.cell.is_null()

    def dump(self):
        """Recursively dump all cells as hex"""

        return self.cell.dump()

    def dump_as_tlb(self, tlb: str) -> str:
        """Dump as C++ PrettyPrint parsed by TLB type"""

        return self.cell.dump_as_tlb(tlb)

    def __repr__(self):
        return self.cell.__repr__()
