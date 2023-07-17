from tonpy.types.tlb import *


class NatWidth(TLB):
    def __init__(self, x: int):
        super().__init__()
        self.size = x
