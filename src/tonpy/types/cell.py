from tonpy.libs.python_ton import PyCell, parseStringToCell
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
        return CellSlice(self.cell.begin_parse())
