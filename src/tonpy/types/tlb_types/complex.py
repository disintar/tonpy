# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.types.tlb import TLB
from tonpy.types.tlb_types.reft import RefT, FakeCell, tAny
from tonpy.types.tlb_types.nat import NatWidth


class TLBComplex(TLB):
    constants = {"t_RefCell": RefT(FakeCell()),
                 "t_Nat": NatWidth(32),
                 "t_Cell": FakeCell(),
                 "t_Anything": tAny()}

    def __init__(self):
        super().__init__()
