from tonpy.types.tlb import *


class NatWidth(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint(self.size)


class NatLess(TLB):
    def __init__(self, x):
        super().__init__()
        self.upper_bound = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint_less(self.upper_bound)


class NatLeq(TLB):
    def __init__(self, x):
        super().__init__()
        self.upper_bound = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint_leq(self.upper_bound)
