from tonpy.libs.python_ton import PyCellSlice, parseStringToCell
from typing import Union


class CellSlice:
    def __init__(self, cs: Union[PyCellSlice, str]):
        """
        CellSlice allow you to read data from cell in two ways:
            - Fetching data and move cursor
            - Prefetching data not moving cursor position

        :param cs: PyCellSlice (c++) or BOC str
        """

        if isinstance(cs, str):
            self.cell_slice: PyCellSlice = parseStringToCell(cs).begin_parse()
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

    def load_uint(self, n: int) -> int:
        """
        Load unsigned integer in `n` bits (up to 256) and move cursor to `n` bits

        :param n: Num of bits to load from CellSlice
        :return: Unsigned integer which was stored in `n` bits
        """

        return int(self.cell_slice.load_uint(n))

    def load_int(self, n: int) -> int:
        """
        Load signed integer in `n` bits (up to 256) and move cursor to `n` bits

        :param n: Num of bits to load from CellSlice
        :return: Integer which was stored in `n` bits
        """

        return int(self.cell_slice.load_int(n))

    def load_var_uint(self, bits: int) -> int:
        """
        Load `VarUInteger bits`, more information can be found in CellBuilder `load_ver_uint` method

        :param bits: Up to what bitsize unsigned integer will be loaded
        :return: Load integer stored in `VarUInteger bits`
        """

        return int(self.cell_slice.load_var_integer_str(bits, False))

    def load_var_int(self, bits: int) -> int:
        """
        Same as `load_var_uint`, but signed

        :param bits: Up to what bitsize integer will be loaded
        :return: Load integer stored in `VarInteger bits`
        """

        return int(self.cell_slice.load_var_integer_str(bits, True))

    def load_address(self) -> str:
        """
        Parse address by `MsgAddress` TLB structure and dump as string

        :return: Loaded address dumped as string
        """

        return self.cell_slice.load_addr()
