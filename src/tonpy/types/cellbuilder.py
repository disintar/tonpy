# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from typing import Union, TYPE_CHECKING

from tonpy.libs.python_ton import PyCellBuilder
from tonpy.types.cell import Cell
from tonpy.types.cellslice import CellSlice
from bitstring import BitArray

from tonpy.types.address import Address
from tonpy.utils.bit_int import test_value_len

if TYPE_CHECKING:
    from tonpy.types.tlb import TLB


class CellBuilder:
    def __init__(self, builder=None):
        """CellBuilder class allow you to create cells"""
        if builder is None:
            self.builder: PyCellBuilder = PyCellBuilder()
        elif isinstance(builder, str):
            self.builder: PyCellBuilder = PyCellBuilder()
            self.store_slice(CellSlice(builder))
        elif isinstance(builder, PyCellBuilder):
            self.builder = builder
        else:
            raise ValueError(f"{type(builder)} for CellBuilder is not supported")

    def store_libref(self, hash_: "str | int"):
        """Create and store special library cell with hash of library cell"""

        if isinstance(hash_, str):
            hash_ = int(hash_, 16)

        c = CellBuilder() \
            .store_uint(CellSlice.SpecialType.Library.value, 8) \
            .store_uint(hash_, 256) \
            .end_cell(special=True)

        self.builder.store_ref(c.cell)
        return self

    @property
    def bits(self) -> int:
        """Bits num that been used in cell"""

        return self.builder.bits

    @property
    def refs(self) -> int:
        """Refs num that been used in cell"""

        return self.builder.refs

    @property
    def remaining_bits(self) -> int:
        """Remaining bits in cell"""

        return self.builder.remaining_bits

    @property
    def remaining_refs(self) -> int:
        """Refs num that been used in cell"""

        return self.builder.remaining_refs

    def store_ref(self, cell: Cell) -> "CellBuilder":
        """
        Take cell and store it to next reference in current builder  |br|

        :param cell: Cell to be stored as reference to current builder
        :return: Updated (self) builder with new reference to cell
        """
        self.builder.store_ref(cell.cell)
        return self

    def store_ref_or_tlb(self, cell: Union[Cell, "TLB.Record"]):
        if not isinstance(cell, Cell):
            cell = cell.cell_pack()

        return self.store_ref(cell)

    def store_builder(self, b: "CellBuilder") -> "CellBuilder":
        """
        Append CellBuilder (bits & refs) ``b`` to current builder  |br|

        :param b: CellBuilder that will be appended to this builder
        :return: Current CellBuilder
        """
        self.builder.store_builder(b.builder)
        return self

    def store_uint(self, uint_: int, uint_bits: int) -> "CellBuilder":
        """
        Stores ``uint_`` unsigned integer with ``uint_bits`` size (up to 256) to current cell  |br|

        :param uint_: Unsigned integer to be stored into cell
        :param uint_bits: Bits num that will be used to store integer to cell
        :return: Current CellBuilder
        """

        if uint_ < 0:
            raise ValueError("Only unsigned integers supported")

        if uint_bits > 256:
            raise ValueError("Max value for int_bits is 256")

        test_value_len(uint_, uint_bits)

        # Large ints need to be converted to string to be parsed in C++
        self.builder.store_uint_str(str(int(uint_)), uint_bits)
        return self

    def store_uint_big(self, a, b):
        self.builder.store_256uint_str(str(a), b)
        return self

    def begin_parse(self) -> CellSlice:
        """Convert CellBuilder to CellSlice"""

        return self.end_cell().begin_parse()

    def store_int(self, int_: int, int_bits: int) -> "CellBuilder":
        """
        Stores ``int_`` integer with ``int_bits`` size (up to 257) to current cell  |br|

        :param int_: Integer to be stored into cell
        :param int_bits: Bits num that will be used to store integer to cell
        :return: Current CellBuilder
        """

        if int_bits > 257:
            raise ValueError("Max value for int_bits is 257")

        test_value_len(int_, int_bits)

        self.builder.store_int_str(str(int_), int_bits)
        return self

    def store_slice(self, cs: CellSlice) -> "CellBuilder":
        """
        Append CellSlice ``b`` (bits & refs) to current CellBuilder  |br|

        :param cs: CellSlice that will be appended to this builder
        :return: Current CellBuilder
        """

        assert isinstance(cs, CellSlice), "Only CellSlice supported"

        self.builder.store_slice(cs.cell_slice)
        return self

    def store_slice_or_tlb(self, cs: Union[CellSlice, "TLB.Record"]):
        """Allow to append cell slice or TLB field"""

        if not isinstance(cs, CellSlice):
            cs = cs.cell_pack().begin_parse()

        return self.store_slice(cs)

    def store_slice_or_tlb_ext(self, cs: Union[CellSlice, "TLB.Record"], ext):
        if not isinstance(cs, CellSlice):
            cs = cs.cell_pack().begin_parse()

        assert cs.size_ext() == ext, f"Expected: {hex(ext)}, got: {cs.size_ext()}"
        return self.store_slice_or_tlb(cs)

    def store_zeroes(self, n: int) -> "CellBuilder":
        """
        Store ``n`` 0 bits to current CellBuilder  |br|

        :param n: Num of 0 bits to be stored
        :return: Current CellBuilder
        """

        if n < 0:
            raise ValueError("Only unsigned integer supported")

        self.builder.store_zeroes(n)

        return self

    def store_ones(self, n: int) -> "CellBuilder":
        """
        Store ``n`` 1 bits to current CellBuilder  |br|

        :param n: Num of 1 bits to be stored
        :return: Current CellBuilder
        """

        if n < 0:
            raise ValueError("Only unsigned integer supported")

        self.builder.store_ones(n)

        return self

    def store_var_uint(self, uint_: int, bits: int) -> "CellBuilder":
        """
        Store ``VarUInteger bits`` to CellSlice  |br|

        The main idea that we store size of our integer in first up to ``bits`` in Cell  |br|
        So we can use less space when storing large integers  |br|

        TLB scheme:  |br|

        .. code-block::

            var_uint$_ {n:#} len:(#< n) value:(uint (len * 8))
              = VarUInteger n;


        :param uint_: Unsigned integer to be stored
        :param bits: Num of bits for VarUInteger
        :return: Current CellBuilder
        """

        if uint_ < 0:
            raise ValueError("Only unsigned integers supported")

        self.builder.store_var_integer(str(uint_), bits, False)
        return self

    def store_var_int(self, int_: int, bits: int) -> "CellBuilder":
        """
        Same as ``store_var_uint`` but work with integers  |br|

        TLB Scheme:  |br|

        .. code-block::

            var_int$_ {n:#} len:(#< n) value:(int (len * 8))
              = VarInteger n;


        :param int_: Signed integer to be stored
        :param bits: Num of bits for VarInteger
        :return: Current CellBuilder
        """

        self.builder.store_var_integer(str(int_), bits, True)
        return self

    def store_uint_less(self, upper_bound: int, value: int) -> "CellBuilder":
        """
        Store ``value`` less than ``upper_bound`` unsigned integer stored as ``bitCount(upper_bound - 1)`` bits  |br|

        :param upper_bound: Max unsigned integer that can be stored
        :param value: Value to store
        :return: Current CellBuilder
        """

        if value > upper_bound - 1:
            raise ValueError("Value can't be upper than upper_bound - 1")

        if upper_bound < 0:
            raise ValueError("Upper bound can't be less then zero in unsigned int")

        if value < 0:
            raise ValueError("Only unsigned integer supported")

        self.builder.store_uint_less(upper_bound, str(value))
        return self

    def store_uint_leq(self, upper_bound: int, value: int) -> "CellBuilder":
        """
        Store ``value`` less or equal than ``upper_bound`` unsigned integer stored as ``bitCount(upper_bound)`` bits  |br|

        :param upper_bound: Max unsigned integer that can be stored
        :param value: Value to store
        :return: Current CellBuilder
        """

        if value > upper_bound:
            raise ValueError("Value can't be upper than upper_bound")

        if upper_bound < 0:
            raise ValueError("Upper bound can't be less then zero in unsigned int")

        if value < 0:
            raise ValueError("Only unsigned integer supported")

        self.builder.store_uint_leq(upper_bound, str(value))
        return self

    def store_bitstring(self, bitstring: Union[str, BitArray]) -> "CellBuilder":
        """
        Store bits from ``bitstring`` string  |br|

        :param bitstring: Bits to store to cell (ex. '11001')
        :return: Current CellBuilder
        """

        if isinstance(bitstring, BitArray):
            bitstring = bitstring.bin

        self.builder.store_bitstring(bitstring)
        return self

    def store_bitstring_chk(self, bitstring: Union[str, BitArray], size):
        assert len(bitstring) <= size
        if isinstance(bitstring, BitArray):
            bitstring = bitstring.bin

        if len(bitstring) < size:
            bitstring = bitstring.zfill(size)

        return self.store_bitstring(bitstring)

    def end_cell(self, special=False) -> Cell:
        """Convert CellBuilder to Cell, if special is True - convert cell to special"""

        return Cell(self.builder.get_cell(special))

    def to_boc(self) -> str:
        """Convert CellBuilder to BOC string"""

        return self.builder.to_boc()

    def dump(self) -> str:
        """Recursively dump all cells as hex"""

        return self.builder.dump()

    def dump_as_tlb(self, tlb: str) -> str:
        """Dump as C++ PrettyPrint parsed by TLB type"""

        return self.builder.dump_as_tlb(tlb)

    def get_hash(self) -> str:
        """Get hash of cell"""

        return self.builder.get_hash()

    def store_grams(self, grams: int) -> "CellBuilder":
        """
        Same as store ``.store_var_uint(grams, 16)``, grams is nanoTON value  |br|

        :param grams: nano TON value to store
        :return: Current CellBuilder
        """

        self.builder.store_grams_str(str(grams))
        return self

    def store_address(self, address: Union[str, "Address"]) -> "CellBuilder":
        """
        Parse smart-contract address from string and store as ``MsgAddress`` TLB structure  |br|

        :param address: Smart-contract address in any format
        :return: Current CellBuilder
        """

        if isinstance(address, str):
            address = Address(address)
        address.append_to_builder(self)

        return self

    def _store_string_rec(self, binstrint_to_store: str) -> Cell:
        """Store bitsring as chain of cells"""

        bits_in_bitstring = len(binstrint_to_store)
        cb = CellBuilder()
        reamining = cb.remaining_bits

        if reamining > bits_in_bitstring:
            cb.store_bitstring(binstrint_to_store)
            return cb.end_cell()
        else:
            body = binstrint_to_store[:reamining]
            tail = binstrint_to_store[reamining:]
            cb.store_bitstring(body)
            return cb.store_ref(self._store_string_rec(tail)).end_cell()

    def store_string(self, string_to_store: str) -> "CellBuilder":
        """
        Convert string ``string_to_store`` to bitstring and store it in chain of cells  |br|

        :param string_to_store: string to be stored
        :return: current CellBuilder
        """
        string_as_bitstring = ''.join(format(byte, '08b') for byte in string_to_store.encode('utf-8'))

        reamining = self.builder.remaining_bits

        if reamining > len(string_as_bitstring):
            self.builder.store_bitstring(string_as_bitstring)
        else:
            body = string_as_bitstring[:reamining]
            tail = string_as_bitstring[reamining:]

            self.builder.store_bitstring(body)
            tail_cell = self._store_string_rec(tail)
            self.store_ref(tail_cell)

        return self

    def store_bool(self, bool_: bool) -> "CellBuilder":
        """Store bool ``bool_`` as 1 bit to current CellBuilder and return modified self"""
        if bool(bool_) is True:
            self.store_uint(1, 1)
        else:
            self.store_uint(0, 1)

        return self

    def __getstate__(self):
        return self.to_boc()

    def __setstate__(self, boc):
        self.builder: PyCellBuilder = PyCellBuilder()
        self.store_slice(Cell(boc).begin_parse())

    def __repr__(self):
        b = self.bits
        r = self.refs

        return f"<CellBuilder [{b}] bits, [{r}] refs, [{self.get_hash()}] hash>"
