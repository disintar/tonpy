from tonpy.types.tlb import *


class Int(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_int(self.size)


class UInt(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint(self.size)


class Bits(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> str:
        return cs.load_bitstring(self.size)
