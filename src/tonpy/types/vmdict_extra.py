from tonpy.types.vmdict import AugmentedData
from tonpy.types.cellslice import CellSlice
from typing import Optional


class SkipCryptoCurrency(AugmentedData):
    def skip_extra(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        cs.load_var_uint(16)

        has_ref = cs.preload_bool()
        if has_ref:
            cs.advance(0x10001)
        else:
            cs.advance(1)

        return True, cs
