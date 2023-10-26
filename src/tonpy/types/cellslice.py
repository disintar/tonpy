# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import PyCellSlice, parse_string_to_cell, load_as_cell_slice
from typing import Union
from enum import Enum
from typing import TYPE_CHECKING

from tonpy.utils.bit_converter import bitstring_to_utf8

if TYPE_CHECKING:
    from tonpy.types.address import Address
    from tonpy.types import Cell


class CellSlice:
    class SpecialType(Enum):
        Ordinary = 0
        PrunnedBranch = 1
        Library = 2
        MerkleProof = 3
        MerkleUpdate = 4

    def __init__(self, cs: Union[PyCellSlice, str], allow_special: bool = False):
        """
        CellSlice allow you to read data from cell in two ways:  |br|

            - Fetching data and move cursor  |br|
            - Prefetching data not moving cursor position

        :param cs: PyCellSlice (c++) or BOC str
        :param allow_special: Allow to load special cells
        :return:
        """

        self.allow_special = allow_special

        if isinstance(cs, str):
            self.cell_slice: PyCellSlice = load_as_cell_slice(parse_string_to_cell(cs), self.allow_special)
        elif isinstance(cs, PyCellSlice):
            self.cell_slice: PyCellSlice = cs
        else:
            raise ValueError(f"PyCellSlice or BOC string is allowed, got {type(cs)}")

    @property
    def bits(self) -> int:
        """Bits num that been used in cell"""

        return self.cell_slice.bits

    @property
    def refs(self) -> int:
        """Refs num that been used in cell"""

        return self.cell_slice.refs

    def is_special(self) -> bool:
        """Is current cell in special"""
        return self.cell_slice.is_special()

    def special_type(self) -> "CellSlice.SpecialType":
        return CellSlice.SpecialType(self.cell_slice.special_type())

    def load_uint(self, n: int) -> int:
        """
        Load unsigned integer in ``n`` bits (up to 256) and move cursor to ``n`` bits  |br|

        :param n: Num of bits to load from CellSlice
        :return: Unsigned integer which was stored in ``n`` bits
        """

        return int(self.cell_slice.load_uint(n))

    def preload_uint(self, n: int) -> int:
        """
        Preload unsigned integer in ``n`` bits (up to 256) and don't change cursor position  |br|

        :param n: Num of bits to load from CellSlice
        :return: Unsigned integer which was stored in ``n`` bits
        """

        return int(self.cell_slice.preload_uint(n))

    def load_int(self, n: int) -> int:
        """
        Load signed integer in ``n`` bits (up to 256) and move cursor to ``n`` bits  |br|

        :param n: Num of bits to load from CellSlice
        :return: Integer which was stored in ``n`` bits
        """

        return int(self.cell_slice.load_int(n))

    def preload_int(self, n: int) -> int:
        """
        Load signed integer in ``n`` bits (up to 256) and don't change cursor position  |br|

        :param n: Num of bits to load from CellSlice
        :return: Integer which was stored in ``n`` bits
        """

        return int(self.cell_slice.preload_int(n))

    def load_var_uint(self, bits: int) -> int:
        """
        Load ``VarUInteger bits``, more information can be found in CellBuilder ``load_ver_uint`` method  |br|

        :param bits: Up to what bitsize unsigned integer will be loaded
        :return: Load integer stored in ``VarUInteger bits``
        """

        return int(self.cell_slice.load_var_integer_str(bits, False))

    def load_var_int(self, bits: int) -> int:
        """
        Same as ``load_var_uint``, but signed  |br|

        :param bits: Up to what bitsize integer will be loaded
        :return: Load integer stored in ``VarInteger bits``
        """

        return int(self.cell_slice.load_var_integer_str(bits, True))

    def load_address(self) -> "Address":
        """
        Parse address by ``MsgAddress`` TLB structure |br|

        :return: Loaded address dumped as string
        """
        from tonpy.types.address import Address

        return Address(self.cell_slice)

    def to_bitstring(self) -> str:
        """
        Dump current CellSlice to bitstring (ex. ``11100011``)  |br|

        :return: Bitstring which is contains in CellSlice
        """

        return self.cell_slice.to_bitstring()

    def to_boc(self) -> str:
        """
        Dump current CellSlice as BOC string  |br|

        :return: Bag of cells string
        """

        return self.cell_slice.to_boc()

    def bit_at(self, position: int) -> int:
        """
        :param position: Bit position to fetch from
        :return: Bit at position ``position`` of current CellSlice
        """

        if position < 0 or position > self.bits:
            raise ValueError("Unreachable position")

        return int(self.cell_slice.bit_at(position))

    def get_hash(self) -> str:
        """Get hash of cell"""

        return self.cell_slice.get_hash()

    def _load_string_cell_chain(self, bit_size: int = 0) -> str:
        """Recursively load string from CellChain"""

        cs = self.load_ref(as_cs=True)
        self.cell_slice = cs.cell_slice

        if self.refs > 0:
            if bit_size != 0:
                if bit_size >= self.bits:
                    bit_size -= self.bits
                else:
                    text = self.to_bitstring()[:bit_size]
                    self.skip_bits(bit_size)

                    # reach end of bit_size
                    return text

            body = self.to_bitstring()
            return body + self._load_string_cell_chain(bit_size)

        if bit_size > self.bits:
            raise ValueError("Not enough bits to upack")

        if bit_size > 0:
            text = self.to_bitstring()[:bit_size]
        else:
            text = self.to_bitstring()

        self.skip_bits(bit_size)

        return text

    def skip_bits(self, bits: int, last: bool = False) -> True:
        """
        Move bits cursor position at ``bits`` bits.  |br|

        :param bits: How many bits to move cursor to
        :param last: If true will reduce the right boundary
        :return: True
        """

        if bits > self.bits:
            raise ValueError("Ambitious bit skip")

        return self.cell_slice.skip_bits(bits, last)

    def skip_refs(self, refs: int, last: bool = False) -> bool:
        """
        Move refs cursor position at ``refs`` count.  |br|

        :param refs: How many refs to move cursor to
        :param last: If true will reduce the right boundary
        :return: True
        """

        if refs > self.refs:
            raise ValueError("Ambitious refs skip")

        return self.cell_slice.skip_refs(refs, last)

    def load_string(self, bit_size: int = 0, cell_chain: bool = True, strict: bool = True) -> str:
        """
        Concatenate all refs to one bit bitstring and load it as string  |br|

        Warning: this will change current cell to last cell in CellChain if ``cell_chain`` is ``True``  |br|


        :param strict If strict will fail if ``all_bits % 8 != 0`` at the end
        :param bit_size: Size of string (in bits) to be loaded (by default all bits in cell)
        :param cell_chain: If False will load only current cell, if True will load all cells by 1 ref in each cell (CellChain)
        :return: String that was loaded
        """

        if bit_size == 0:
            body = self.to_bitstring()
        else:
            if bit_size <= self.bits:
                text = self.to_bitstring()[:bit_size]
                self.skip_bits(bit_size)
                return bitstring_to_utf8(text, strict)
            else:
                bit_size -= self.bits
                body = self.to_bitstring()

        if cell_chain and self.refs > 0:
            return bitstring_to_utf8(body + self._load_string_cell_chain(bit_size), strict)
        else:
            if bit_size != 0:
                raise ValueError("Not enough bits in current cell. Cell chain is False.")

            return bitstring_to_utf8(body, strict)

    def load_ref(self, offset: int = 0, as_cs: bool = False) -> Union["Cell", "CellSlice"]:
        """
        Fetches cell on next reference and return it, move refs cursor position by 1  |br|

        :param offset: Skip first ``offset`` refs
        :param as_cs: If ``True`` will convert loaded Cell to CellSlice
        :return: New CellSlice from cell stored in next ref
        """
        from tonpy.types import Cell

        if offset > 0:
            self.skip_refs(offset)

        val = Cell(self.cell_slice.fetch_ref())

        if as_cs:
            val = val.begin_parse()

        return val

    def preload_ref(self, offset: int = 0, as_cs: bool = False) -> Union["Cell", "CellSlice"]:
        """
        Fetches cell on next reference and return it, don't change refs cursor position  |br|

        :param offset: Skip first ``offset`` refs (but don't move pointer position)
        :param as_cs: If ``True`` will convert loaded Cell to CellSlice
        :return: New CellSlice from cell stored in next ref
        """
        from tonpy.types import Cell

        val = Cell(self.cell_slice.prefetch_ref(offset))

        if as_cs:
            val = val.begin_parse()

        return val

    def size_ext(self):
        """Get size in ext format:  |br|

        .. code-block::

            refs = bits_refs // (2 ** 16)
            bits = bits_refs % (2 ** 16)
        """
        return self.cell_slice.size_ext()

    def advance_ext(self, bits_refs: int) -> True:
        """
        Try to skip ``bits`` and ``refs``, return False if ``(refs > self.refs) or (bits > self.bits)`` |br|

        :param bits_refs: ``num_bits * (2**16) + num_refs``
        :return: Is operation is success
        """

        return self.cell_slice.advance_ext(bits_refs)

    def advance(self, bits: int) -> bool:
        """
        Try to skip ``bits``, return False if ``bits >= self.bits``  |br|

        :param bits: Num of bits to try to skip
        :return: Is skip was success
        """

        return self.cell_slice.advance(bits)

    def advance_refs(self, refs: int) -> bool:
        """
        Try to skip ``refs``, return False if ``refs >= self.refs``  |br|

        :param refs: Num of refs to try to skip
        :return: Is skip was success
        """

        return self.cell_slice.advance_refs(refs)

    def advance_bits_refs(self, bits: int, refs: int) -> bool:
        """
        Try to skip ``bits`` and ``refs``, return False if ``(refs > self.refs) or (bits > self.bits)``  |br|

        :param bits: Num bits of try to skip
        :param refs: Num refs of try to skip
        :return: Is operation success
        """

        return self.cell_slice.advance_bits_refs(bits, refs)

    def dump_as_tlb(self, tlb: str) -> str:
        """Dump as C++ PrettyPrint parsed by TLB type"""

        return self.cell_slice.dump_as_tlb(tlb)

    def load_tlb(self, tlb_structure: str) -> "CellSlice":
        """
        Load as C++ defined tlb structure from block.tlb, store to new CellSlice, move pointer  |br|

        :param tlb_structure: Class name of TLB to load
        :return: New cell slice contains TLB structure
        """

        return CellSlice(self.cell_slice.load_tlb(tlb_structure))

    def dump(self) -> str:
        """Recursively dump all cells as hex"""

        return self.cell_slice.dump()

    def bselect(self, bits: int, mask: int) -> int:
        """
        Unsigned integer ``bits``: ``0b111``  |br|
        Mask: ``0b11111111`` (up to 8 variants)  |br|
        Result: 7  |br|


        :param bits: Num bits (up to 6) to load unsigned integer (X)
        :param mask: Mask that will be applied to ones bitstring length of X+1
        :return: Count of ones after mask is applied or ``-1`` if not enough bits or bits > 6
        """

        return int(self.cell_slice.bselect(bits, str(mask)))

    def bselect_ext(self, bits: int, mask: int) -> int:
        """
        Same as bselect, but allow to < then ``bits`` (they will be padded)  |br|

        :param bits: Num bits (up to 6) to load unsigned integer (X)
        :param mask: Mask that will be applied to ones bitstring length of X+1
        :return: Count of ones after mask is applied or ``-1`` if not enough bits or bits > 6
        """

        return int(self.cell_slice.bselect_ext(bits, str(mask)))

    def empty_ext(self) -> bool:
        """Is current CellSlice is empty (no bits, no refs)"""

        return self.cell_slice.empty_ext()

    def load_bool(self) -> bool:
        """Load 1 bit from current CellSlice and return it as bool"""
        return bool(self.load_uint(1))

    def preload_bool(self) -> bool:
        """Preload 1 bit from current CellSlice and return it as bool"""
        return bool(self.preload_uint(1))

    def load_uint_leq(self, upper_bound: int) -> int:
        """Load value less or equal than ``upper_bound`` unsigned integer stored as ``bitCount(upper_bound)`` bits"""

        return self.cell_slice.fetch_uint_leq(upper_bound)

    def load_uint_less(self, upper_bound: int) -> int:
        """Load value less than ``upper_bound`` unsigned integer stored as ``bitCount(upper_bound - 1)`` bits"""

        return self.cell_slice.fetch_uint_less(upper_bound)

    def load_bitstring(self, size: int) -> str:
        """Load bitstring of ``size`` bits and move cursor"""

        if self.bits < size:
            raise ValueError("Not enough bits to unpack")

        tmp = self.to_bitstring()[:size]
        self.skip_bits(size)

        return tmp

    def preload_bitstring(self, size: int) -> str:
        """Load bitstring of ``size`` bits"""

        if self.bits < size:
            raise ValueError("Not enough bits to unpack")

        tmp = self.to_bitstring()[:size]

        return tmp

    def load_subslice(self, bits: int, refs: int = 0) -> "CellSlice":
        """Load ``bits`` and ``refs`` to separate ``CellSlice`` and move cursor"""

        return CellSlice(self.cell_slice.load_subslice(bits, refs))

    def preload_subslice(self, bits: int, refs: int = 0) -> "CellSlice":
        """Load ``bits`` and ``refs`` to separate ``CellSlice``"""

        return CellSlice(self.cell_slice.preload_subslice(bits, refs))

    def load_subslice_ext(self, bits_refs: int) -> "CellSlice":
        """Same as ``load_subslice`` but in ``ext`` size format

        .. code-block::

            refs = bits_refs // (2 ** 16)
            bits = bits_refs % (2 ** 16)

        """

        return CellSlice(self.cell_slice.load_subslice_ext(bits_refs))

    def preload_subslice_ext(self, bits_refs: int) -> "CellSlice":
        """Same as ``preload_subslice`` but in ``ext`` size format

        .. code-block::

            refs = bits_refs // (2 ** 16)
            bits = bits_refs % (2 ** 16)

        """

        return CellSlice(self.cell_slice.preload_subslice_ext(bits_refs))

    def cut_tail(self, cs: "CellSlice") -> bool:
        """Skip ``bits`` & ``refs`` of ``cs`` from current ``CellSlice``"""
        return self.cell_slice.cut_tail(cs.cell_slice)

    def copy(self) -> "CellSlice":
        """Make independent copy of current ``CellSlice``"""
        return CellSlice(self.cell_slice.copy())

    def to_cell(self) -> "Cell":
        # TODO: find better way (c++?)
        from tonpy.types import CellBuilder
        cb = CellBuilder()
        cb.store_slice(self)
        return cb.end_cell(self.allow_special)

    def __getstate__(self):
        return [self.to_boc(), self.allow_special]

    def __setstate__(self, boc_special):
        boc, allow_special = boc_special

        self.allow_special = allow_special
        self.cell_slice: PyCellSlice = load_as_cell_slice(parse_string_to_cell(boc), self.allow_special)

    def __repr__(self):
        b = self.bits
        r = self.refs

        return f"<CellSlice [{b}] bits, [{r}] refs, [{self.get_hash()}] hash>"
