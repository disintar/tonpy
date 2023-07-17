from tonpy.types.tlb import TLB
from tonpy.types.tlb_types.reft import RefT, FakeCell


class TLBComplex(TLB):
    constants = {"t_RefCell": RefT(FakeCell())}

    def __init__(self):
        super().__init__()
