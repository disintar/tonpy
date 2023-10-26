# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.types.tlb import *


class NatWidth(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x

    def args_pack(self, cb: CellBuilder, x: int):
        cb.store_uint(x, self.size)

    def args_cell_pack(self, x: int):
        cb = CellBuilder()
        self.args_pack(cb, x)
        return cb.end_cell().begin_parse()

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint(self.size)

    def store_ref_or_tlb(self, cb: CellBuilder, value):
        return cb.store_ref(CellBuilder().store_uint(value, self.size).end_cell())


class NatLess(TLB):
    def __init__(self, x):
        super().__init__()
        self.upper_bound = x

    def args_pack(self, cb: CellBuilder, x: int):
        cb.store_uint_less(self.upper_bound, x)

    def args_cell_pack(self, x: int):
        cb = CellBuilder()
        self.args_pack(cb, x)
        return cb.end_cell().begin_parse()

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint_less(self.upper_bound)

    def store_ref_or_tlb(self, cb: CellBuilder, value):
        return cb.store_ref(CellBuilder().store_uint_less(self.upper_bound, value).end_cell())


class NatLeq(TLB):
    def __init__(self, x):
        super().__init__()
        self.upper_bound = x

    def args_pack(self, cb: CellBuilder, x: int):
        cb.store_uint_leq(self.upper_bound, x)

    def args_cell_pack(self, x: int):
        cb = CellBuilder()
        self.args_pack(cb, x)
        return cb.end_cell().begin_parse()

    def unpack(self, cs: CellSlice, rec_unpack: bool = False, strict: bool = False) -> int:
        return cs.load_uint_leq(self.upper_bound)

    def store_ref_or_tlb(self, cb: CellBuilder, value):
        return cb.store_ref(CellBuilder().store_uint_leq(self.upper_bound, value).end_cell())
