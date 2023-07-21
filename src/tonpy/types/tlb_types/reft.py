from tonpy.types.tlb import *


class RefT(TLB):
    """TLB Ref type ``^T``"""

    def __init__(self, x: TLB):
        super().__init__()
        self.type = x

    def fetch(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = False) -> "Optional[TLB.Record]":
        """ Load first ref from CellSlice and unpack as type """

        assert isinstance(cell_ref, Cell)
        self.original_cell = cell_ref

        return self.type.fetch(cell_ref, rec_unpack)


class FakeCell(TLB):
    def fetch(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = False) -> "Optional[TLB.Record]":
        assert isinstance(cell_ref, Cell)
        self.original_cell = cell_ref
        return cell_ref
