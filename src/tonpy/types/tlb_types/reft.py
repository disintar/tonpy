from tonpy.types.tlb import *


class RefT(TLB):
    """TLB Ref type ``^T``"""

    def __init__(self, x: TLB):
        super().__init__()
        self.type = x

    def fetch(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = False, load_ref: bool = False,
              **kwargs) -> "Optional[TLB.Record]":
        """ Load first ref from CellSlice and unpack as type """

        if load_ref:
            assert isinstance(cell_ref, CellSlice)
            cell_ref = cell_ref.load_ref()

        if isinstance(cell_ref, Cell):
            self.original_cell = cell_ref
        else:
            self.original_cell_slice = cell_ref

        return self.type.fetch(cell_ref, rec_unpack, strict)


class FakeCell(TLB):
    def fetch(self, cell_ref: Cell, rec_unpack: bool = False, strict: bool = False, **kwargs) -> "Optional[TLB.Record]":
        assert isinstance(cell_ref, Cell)
        self.original_cell = cell_ref
        return cell_ref


class tAny(TLB):
    def fetch(self, c: Union[Cell, CellSlice], rec_unpack: bool = False,
              strict: bool = False, **kwargs) -> "Optional[TLB.Record]":
        if isinstance(c, Cell):
            self.original_cell = c
            return c
        else:
            self.original_cell_slice = c.load_subslice(c.bits, c.refs)
            return self.original_cell_slice
