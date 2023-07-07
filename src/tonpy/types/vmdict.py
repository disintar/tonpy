from typing import Union, Iterable

from tonpy.libs.python_ton import PyDict

from tonpy.types.cell import Cell
from tonpy.types.cellslice import CellSlice
from tonpy.types.cellbuilder import CellBuilder
from tonpy.utils.bit_int import test_value_len


#       .def("set_ref_str", &PyDict::set_ref, py::arg("key"), py::arg("value"), py::arg("mode") = "set",
#            py::arg("key_len") = 0, py::arg("signed") = false)
#       .def("set_builder_str", &PyDict::set_builder, py::arg("key"), py::arg("value"), py::arg("mode") = "set",
#            py::arg("key_len") = 0, py::arg("signed") = false)
#       .def("get_minmax_key_ref", &PyDict::get_minmax_key_ref, py::arg("fetch_max") = false,
#            py::arg("inver_first") = false, py::arg("key_len") = 0, py::arg("signed") = false)
#       .def("lookup_delete_str", &PyDict::lookup_delete, py::arg("key"), py::arg("key_len") = 0,
#            py::arg("signed") = false)
#       .def("lookup_ref_str", &PyDict::lookup_ref, py::arg("key"), py::arg("key_len") = 0, py::arg("signed") = false)
#       .def("lookup_delete_ref_str", &PyDict::lookup_delete_ref, py::arg("key"), py::arg("key_len") = 0,
#            py::arg("signed") = false)
#       .def("__repr__", &PyDict::toString);


class VmDict:
    def __init__(self, key_len: int, signed: bool = False, cell_root: Union[Union[str, Cell], CellSlice] = None):
        """
        Wrapper of HashmapE (dictionary type of TON)

        Key are represented as ``key_len`` bits. They can be loaded as ``signed`` or not.

        .. code-block::

            hm_edge#_ {n:#} {X:Type} {l:#} {m:#} label:(HmLabel ~l n)
                {n = (~m) + l} node:(HashmapNode m X) = Hashmap n X;

            hmn_leaf#_ {X:Type} value:X = HashmapNode 0 X;
            hmn_fork#_ {n:#} {X:Type} left:^(Hashmap n X)
                       right:^(Hashmap n X) = HashmapNode (n + 1) X;

            hml_short$0 {m:#} {n:#} len:(Unary ~n) {n <= m} s:(n * Bit) = HmLabel ~n m;
            hml_long$10 {m:#} n:(#<= m) s:(n * Bit) = HmLabel ~n m;
            hml_same$11 {m:#} v:Bit n:(#<= m) = HmLabel ~n m;

            unary_zero$0 = Unary ~0;
            unary_succ$1 {n:#} x:(Unary ~n) = Unary ~(n + 1);

            hme_empty$0 {n:#} {X:Type} = HashmapE n X;
            hme_root$1 {n:#} {X:Type} root:^(Hashmap n X) = HashmapE n X;

        :param key_len: Size of keys in bits (up to 257 with ``signed`` or 256)
        :param signed: Load keys as signed integers or not
        :param cell_root: Root of HashmapE, can be BOC string, CellSlice or Cell
        """

        if key_len > 256:
            if not (key_len == 257 and signed):
                raise ValueError("Key len must not be larger than 256 for unsigned / 257 for signed")

        self.key_len = key_len
        self.signed = signed

        if cell_root is not None:
            cs = cell_root

            if isinstance(cs, str):
                cs = CellSlice(cs)
            elif isinstance(cs, Cell):
                cs = cs.begin_parse()

            cell_root = cs.cell_slice

        self.dict = PyDict(key_len, signed, cell_root)

    def _process_sgnd(self, key: int = None, signed: bool = None) -> bool:
        """Check ``key`` to be ``signed`` or if ``signed`` is None will use current dict ``self.signed``"""
        if signed is None:
            signed = self.signed

        if key is not None:
            if key < 0 and (signed is False):
                raise ValueError(f"Signed is false, but key < 0")
        return signed

    def set(self, key: int, value: CellSlice, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Add / Set / Replace ``key`` as ``key_len`` and ``signed`` bits to value ``value``

        - Set: sets the value associated with ``key_len``-bit key ``key`` in VmDict to value ``value``

        - Add: sets the value associated with key ``key`` to ``value``, but only if ``key`` is not already present in VmDict

        - Replace: sets the value of ``key`` to ``value`` only if the key ``key`` was already present in VmDict

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """
        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        if not isinstance(value, CellSlice):
            raise ValueError(f"CellSlice needed")

        self.dict.set_str(str(key), value.cell_slice, mode, 0, signed)
        return self

    def is_empty(self) -> bool:
        """If dict contains no keys - it's empty"""
        return self.dict.is_empty()

    def get_cell(self) -> Cell:
        """Get root cell of dictionary"""
        return Cell(self.dict.get_pycell())

    def lookup_nearest_key(self, key: int, fetch_next: bool = True, allow_eq: bool = False,
                           invert_first: bool = True, signed: bool = None) -> tuple[int, CellSlice]:
        """
        Compute the nearest key to ``key``

        :param key: ``self.key_len``-bit integer key
        :param fetch_next: If ``True`` will fetch next else will return prev
        :param allow_eq: If ``True`` will return value with ``key`` if exist
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Founded key and value
        """
        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        key, value = self.dict.lookup_nearest_key(str(key), fetch_next, allow_eq, invert_first, 0, signed)
        return int(key), CellSlice(value)

    def get_minmax_key(self, fetch_max: bool = True, invert_first: bool = True, signed: bool = None) -> tuple[
        int, CellSlice]:
        """
        Fetch max / min ``key, value``

        :param fetch_max: If ``True`` will fetch max key, else will fetch min key in dict
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Key and CellSlice that stored in key
        """
        signed = self._process_sgnd(signed=signed)

        key, value = self.dict.get_minmax_key(fetch_max, invert_first, 0, signed)
        return int(key), CellSlice(value)

    def get_minmax_key_ref(self, fetch_max: bool = True, inver_first: bool = False, signed: bool = None) -> tuple[
        int, Cell]:
        """
        Same as get_minmax, but fetch Cell by key (stored in ref)

        :param fetch_max: If ``True`` will fetch max key, else will fetch min key in dict
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Key and Cell that stored in key
        """

        key, value = self.dict.get_minmax_key_ref(fetch_max, inver_first, 0, signed)
        return int(key), Cell(value)

    def set_ref(self, key: int, value: Cell, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Same as set, but store Cell to ref (by key)

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """

        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        if not isinstance(value, Cell):
            raise ValueError(f"Only Cell accepted as value")

        self.dict.set_ref_str(str(key), value.cell, mode, 0, signed)
        return self

    def set_builder(self, key: int, value: CellBuilder, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Set cell builder stored to ``key``, you can load it by ``lookup`` method

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """

        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        if not isinstance(value, CellBuilder):
            raise ValueError(f"CellBuilder needed")

        self.dict.set_builder_str(str(key), value.builder, mode, 0, signed)
        return self

    def lookup(self, key, key_len=0, signed=-1):
        return CellSlice(self.dict.lookup_str(str(key), 0, signed))

    def lookup_delete(self, key, key_len=0, signed=-1):
        return CellSlice(self.dict.lookup_delete_str(str(key), 0, signed))

    def lookup_ref(self, key, key_len=0, signed=-1):
        return Cell(self.dict.lookup_ref_str(str(key), 0, signed))

    def lookup_delete_ref(self, key, key_len=0, signed=-1):
        return Cell(self.dict.lookup_delete_ref_str(str(key), 0, signed))

    def get_iter(self, direction=False) -> Iterable[tuple[int, CellSlice]]:
        key, value = self.get_minmax_key(direction)
        yield key, value

        while True:
            try:
                key, value = self.lookup_nearest_key(key, not direction)
                yield key, value
            except RuntimeError:
                return

    def __repr__(self):
        return self.dict.__repr__()

    def __iter__(self):
        return self.get_iter(False)

    def __reversed__(self):
        return self.get_iter(True)
