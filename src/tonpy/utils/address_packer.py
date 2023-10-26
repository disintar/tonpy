# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import pack_address as orig_pack_address

from tonpy.types.cellslice import CellSlice


def pack_address(address: str) -> "CellSlice":
    return CellSlice(cs=orig_pack_address(address))
