from tonpy.libs.python_ton import pack_address as orig_pack_address

from tonpy.types.cellslice import CellSlice


def pack_address(address: str) -> "CellSlice":
    return CellSlice(cs=orig_pack_address(address))
