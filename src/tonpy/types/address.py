# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PySmcAddress, address_from_string, address_from_cell_slice
from typing import Union, TYPE_CHECKING, Optional

from tonpy.types.cellslice import CellSlice

if TYPE_CHECKING:
    from tonpy.types.cellbuilder import CellBuilder


class Address:
    def __init__(self, value: Union[str, "CellSlice"] = None):
        """Class allow you to interact with TON SmartContract address"""
        if isinstance(value, str):
            self.my_address: PySmcAddress = address_from_string(value)
            self.type = 'addr_std'
        elif value is None or value == 0:
            self.my_address = None
            self.type = 'addr_none'
        else:
            self.my_address: PySmcAddress = address_from_cell_slice(value)
            self.type = 'addr_std'

    def pack(self) -> "CellSlice":
        return CellSlice(self.my_address.pack())

    @property
    def wc(self) -> Optional[int]:
        if self.my_address is None:
            return None

        return self.my_address.wc

    @wc.setter
    def wc(self, wc: int):
        self.my_address.wc = wc

    @property
    def workchain(self) -> Optional[int]:
        return self.wc

    @workchain.setter
    def workchain(self, wc: int):
        self.wc(wc)

    @property
    def address(self) -> Optional[str]:
        "HEX encoded address"
        if self.my_address is None:
            return None

        return self.my_address.address()

    @property
    def bounceable(self) -> bool:
        if self.my_address is None:
            return False

        return self.my_address.bounceable

    @bounceable.setter
    def bounceable(self, flag: bool):
        if self.my_address is None:
            raise ValueError("Cannot set bounceable to addr_none")

        self.my_address.bounceable = flag

    @property
    def testnet(self) -> bool:
        if self.my_address is None:
            return False

        return self.my_address.testnet

    @property
    def raw(self) -> Union[None, str]:
        if self.my_address is None:
            return None

        return f"{self.wc}:{self.address}"

    @testnet.setter
    def testnet(self, flag: bool):
        if self.my_address is None:
            raise ValueError("Cannot set bounceable to addr_none")

        self.my_address.testnet = flag

    def serialize(self, base64_url: bool = True):
        if self.my_address is None:
            return None

        return self.my_address.rserialize(base64_url)

    def append_to_builder(self, cb: "CellBuilder"):
        if self.my_address is None:
            cb.store_uint(0, 2)
            return

        assert self.my_address.append_to_builder(cb.builder)

    def shard_prefix(self, size) -> int:
        if self.my_address is None:
            raise ValueError("Cannot shard addr_none")

        return self.my_address.shard_prefix(size)

    def to_cs(self) -> CellSlice:
        from tonpy.types.cellbuilder import CellBuilder
        if self.my_address is None:
            return CellBuilder().store_uint(0, 2).end_cell().begin_parse()
        return CellBuilder().store_address(self).end_cell().begin_parse()

    def __eq__(self, other):
        return self.workchain == other.workchain and self.address == other.address

    def __getstate__(self):
        return self.serialize()

    def __setstate__(self, value):
        if value is None:
            self.my_address = None
            self.type = 'addr_none'
            return

        self.my_address: PySmcAddress = address_from_string(value)

    def __str__(self):
        if self.my_address is None:
            return 'addr_none'

        return f'{self.serialize()}'

    def __repr__(self):
        return f'<Address value="{self.serialize()}">'

    def __hash__(self):
        return int(f"{self.wc}{self.address}", 16)

