# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PySmcAddress, address_from_string, address_from_cell_slice
from typing import Union, TYPE_CHECKING

from tonpy.types.cellslice import CellSlice

if TYPE_CHECKING:
    from tonpy.types.cellbuilder import CellBuilder


class Address:
    def __init__(self, value: Union[str, "CellSlice"]):
        """Class allow you to interact with TON SmartContract address"""
        if isinstance(value, str):
            self.my_address: PySmcAddress = address_from_string(value)
        else:
            self.my_address: PySmcAddress = address_from_cell_slice(value)

    def pack(self) -> "CellSlice":
        return CellSlice(self.my_address.pack())

    @property
    def wc(self) -> int:
        return self.my_address.wc

    @wc.setter
    def wc(self, wc: int):
        self.my_address.wc = wc

    @property
    def workchain(self) -> int:
        return self.my_address.wc

    @workchain.setter
    def workchain(self, wc: int):
        self.my_address.wc = wc

    @property
    def address(self) -> str:
        "HEX encoded address"
        return self.my_address.address()

    @property
    def bounceable(self) -> bool:
        return self.my_address.bounceable

    @bounceable.setter
    def bounceable(self, flag: bool):
        self.my_address.bounceable = flag

    @property
    def testnet(self) -> bool:
        return self.my_address.testnet

    @testnet.setter
    def testnet(self, flag: bool):
        self.my_address.testnet = flag

    def serialize(self, base64_url: bool = True):
        return self.my_address.rserialize(base64_url)

    def append_to_builder(self, cb: "CellBuilder"):
        assert self.my_address.append_to_builder(cb.builder)

    def shard_prefix(self, size) -> int:
        return self.my_address.shard_prefix(size)

    def to_cs(self) -> CellSlice:
        return CellBuilder().store_address(self).end_cell().begin_parse()

    def __eq__(self, other):
        # TODO: made this work
        raise NotImplementedError
        # return self.my_address == other.my_address

    def __getstate__(self):
        return self.serialize()

    def __setstate__(self, value):
        self.my_address: PySmcAddress = address_from_string(value)

    def __str__(self):
        return f'{self.serialize()}'

    def __repr__(self):
        return f'<Address value="{self.serialize()}">'
