# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from typing import Union, Iterable, Optional, Tuple, Callable

from tonpy.libs.python_ton import PyDict, PyCellSlice, PyAugmentationCheckData

from tonpy.types.cell import Cell
from tonpy.types.cellslice import CellSlice
from tonpy.types.cellbuilder import CellBuilder
from tonpy.utils.bit_converter import convert_str_to_int
from tonpy.utils.bit_int import test_value_len
from tonpy.types.tlb import TLB


class AugmentedData:
    def eval_leaf(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        """Extract extra from leaf value ``cs``"""
        raise NotImplementedError

    def skip_extra(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        """Skip extra from leaf, return updated ``cs``"""
        raise NotImplementedError

    def eval_fork(self, left: CellSlice, right: CellSlice) -> (bool, Optional[CellSlice]):
        raise NotImplementedError

    def eval_empty(self) -> (bool, Optional[CellSlice]):
        raise NotImplementedError

    def _eval_leaf(self, cs: PyCellSlice):
        answer = list(self.eval_leaf(CellSlice(cs)))

        if len(answer) > 1:
            answer[1] = answer[1].cell_slice
        return tuple(answer)

    def _skip_extra(self, cs: PyCellSlice):
        answer = list(self.skip_extra(CellSlice(cs)))

        if len(answer) > 1:
            answer[1] = answer[1].cell_slice
        return tuple(answer)

    def _eval_fork(self, left: PyCellSlice, right: PyCellSlice):
        answer = list(self.eval_fork(CellSlice(left), CellSlice(right)))

        if len(answer) > 1:
            answer[1] = answer[1].cell_slice
        return tuple(answer)

    def _eval_empty(self):
        answer = list(self.eval_empty())

        if len(answer) > 1:
            answer[1] = answer[1].cell_slice
        return tuple(answer)

    def get_base_aug(self):
        return PyAugmentationCheckData(self._eval_leaf, self._skip_extra,
                                       self._eval_fork, self._eval_empty)


class TypedAugmentedData(AugmentedData):
    def __init__(self, value_type: TLB, extra_type: TLB):
        super(TypedAugmentedData, self).__init__()
        self.value_type = value_type
        self.extra_type = extra_type

    def skip_extra(self, cs: CellSlice) -> (bool, Optional[CellSlice]):
        # TODO: this is slow, use autogen skip when it will be done
        self.extra_type.fetch(cs)
        return True, cs


class DataWithExtra:
    def __init__(self, cs: CellSlice, aug: AugmentedData):
        self.cs_extra = cs
        self.cs_value = cs.copy()
        self.aug = aug
        self.aug.skip_extra(self.cs_value)
        self.cs_extra.cut_tail(self.cs_value)

    @property
    def extra(self):
        return self.cs_extra

    @property
    def data(self):
        return self.cs_value

    def __getitem__(self, item):
        if item == 0 or item == 'extra':
            return self.extra
        elif item == 1 or item == 'data':
            return self.data
        else:
            raise ValueError

    def __repr__(self):
        return f"<DataWithExtra: {str(self.cs_extra)} {str(self.cs_value)}>"


class TypedDataWithExtra(DataWithExtra):
    def __init__(self, cs: CellSlice, aug: TypedAugmentedData, rec_unpack=False):
        super().__init__(cs, aug)
        self.cs_extra = aug.extra_type.fetch(self.cs_extra, rec_unpack)
        self.cs_value = aug.value_type.fetch(self.cs_value, rec_unpack)


class VmDict:
    # TODO: bind for_each / for_each_extra for speed up
    # TODO: made pickable

    def __init__(self, key_len: int,
                 signed: bool = False,
                 cell_root: Union[Union[str, Cell], CellSlice] = None,
                 aug: AugmentedData = None,
                 py_dict: PyDict = None):
        """
        Wrapper of HashmapE (dictionary type of TON)  |br|

        Key are represented as ``key_len`` bits. They can be loaded as ``signed`` or not.  |br|

        :param key_len: Size of keys in bits (up to 257 with ``signed`` or 256)
        :param signed: Load keys as signed integers or not
        :param cell_root: Root of HashmapE, can be BOC string, CellSlice or Cell
        :return:
        """

        self.key_len = key_len
        self.signed = signed

        if py_dict is not None:
            self.dict = py_dict
            if aug is None:
                self.is_augmented = False
            else:
                self.aug = aug
                self.is_augmented = True
            return

        if cell_root is not None:
            cs = cell_root

            if isinstance(cs, str):
                cs = CellSlice(cs)
            elif isinstance(cs, Cell):
                cs = cs.begin_parse()

            cell_root = cs.cell_slice

        if aug is None:
            self.dict = PyDict(bit_len=key_len, signed=signed, cs_root=cell_root)
            self.is_augmented = False
        else:
            self.aug = aug
            self.dict = PyDict(key_len, aug.get_base_aug(), signed, cell_root)
            self.is_augmented = True

    def _process_sgnd(self, key: int = None, signed: bool = None) -> bool:
        """Check ``key`` to be ``signed`` or if ``signed`` is None will use current dict ``self.signed``"""
        if signed is None:
            signed = self.signed

        if key is not None:
            if key < 0 and (signed is False):
                raise ValueError(f"Signed is false, but key < 0")
        return signed

    def is_empty(self) -> bool:
        """If dict contains no keys - it's empty"""
        return self.dict.is_empty()

    def get_cell(self) -> Cell:
        """Get root cell of dictionary"""
        return Cell(self.dict.get_pycell())

    def lookup_nearest_key(self, key: int, fetch_next: bool = True, allow_eq: bool = False,
                           invert_first: bool = True, signed: bool = None) -> tuple[
        int, Union[CellSlice, DataWithExtra]]:
        """
        Compute the nearest key to ``key``  |br|

        :param key: ``self.key_len``-bit integer key
        :param fetch_next: If ``True`` will fetch next else will return prev
        :param allow_eq: If ``True`` will return value with ``key`` if exist
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Founded key and value
        """

        if (self.signed and self.key_len > 256) or self.key_len > 257:
            raise NotImplementedError("Use .map instead")

        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        key, value = self.dict.lookup_nearest_key(str(key), fetch_next, allow_eq, invert_first, 0, signed)
        cs = CellSlice(value)

        if self.is_augmented:
            return int(key), DataWithExtra(cs, self.aug)

        return int(key), cs

    def get_minmax_key(self, fetch_max: bool = True, invert_first: bool = True, signed: bool = None) -> tuple[
        int, Union[CellSlice, DataWithExtra]]:
        """
        Fetch max / min ``key, value``  |br|

        :param fetch_max: If ``True`` will fetch max key, else will fetch min key in dict
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Key and CellSlice that stored in key
        """

        if (self.signed and self.key_len > 256) or self.key_len > 257:
            raise NotImplementedError("Use .map instead")

        signed = self._process_sgnd(signed=signed)

        key, value = self.dict.get_minmax_key(fetch_max, invert_first, 0, signed)
        cs = CellSlice(value)

        if self.is_augmented:
            return int(key), DataWithExtra(cs, self.aug)
        return int(key), cs

    def get_minmax_key_ref(self, fetch_max: bool = True, inver_first: bool = False, signed: bool = None) -> tuple[
        int, Cell]:
        """
        Same as get_minmax, but fetch Cell by key (stored in ref)  |br|

        :param fetch_max: If ``True`` will fetch max key, else will fetch min key in dict
        :param invert_first: If ``True`` will respect ``signed`` in operations
        :param signed: Fetch keys as signed or not
        :return: Key and Cell that stored in key
        """

        if (self.signed and self.key_len > 256) or self.key_len > 257:
            raise NotImplementedError("Use .map instead")

        key, value = self.dict.get_minmax_key_ref(fetch_max, inver_first, 0, signed)
        return int(key), Cell(value)

    def set_keycs(self, key: CellSlice, value: CellSlice, mode: str = "set"):
        if not isinstance(value, CellSlice):
            raise ValueError(f"CellSlice needed")

        self.dict.set_keycs(key.cell_slice, value.cell_slice, mode, 0)
        return self

    def set(self, key: Union[int, CellSlice], value: CellSlice, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Add / Set / Replace ``key`` as ``key_len`` and ``signed`` bits to value ``value``  |br|

        - Set: sets the value associated with ``key_len``-bit key ``key`` in VmDict to value ``value``

        - Add: sets the value associated with key ``key`` to ``value``, but only if ``key`` is not already present in VmDict

        - Replace: sets the value of ``key`` to ``value`` only if the key ``key`` was already present in VmDict

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.set_keycs(key, value, mode)

        if not isinstance(value, CellSlice):
            raise ValueError(f"CellSlice needed")

        self.dict.set_str(str(key), value.cell_slice, mode, 0, signed)
        return self

    def set_ref_keycs(self, key: CellSlice, value: Cell, mode: str = "set"):
        if not isinstance(value, Cell):
            raise ValueError(f"CellSlice needed")

        self.dict.set_ref_keycs(key.cell_slice, value.cell, mode, 0)
        return self

    def set_ref(self, key: int, value: Cell, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Same as set, but store Cell to ref (by key)  |br|

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.set_ref_keycs(key, value, mode)

        if not isinstance(value, Cell):
            raise ValueError(f"Only Cell accepted as value")

        self.dict.set_ref_str(str(key), value.cell, mode, 0, signed)
        return self

    def set_builder_keycs(self, key: CellSlice, value: CellBuilder, mode: str = "set"):
        if not isinstance(value, CellBuilder):
            raise ValueError(f"CellSlice needed")

        self.dict.set_builder_keycs(key.cell_slice, value.builder, mode, 0)
        return self

    def set_builder(self, key: int, value: CellBuilder, mode: str = "set", signed: bool = None) -> "VmDict":
        """
        Set cell builder stored to ``key``, you can load it by ``lookup`` method  |br|

        :param key: Integer to be stored as key
        :param value: CellSlice to be stored
        :param mode: "set" / "replace" / "add"
        :param signed: Signed
        :return: Updated self
        """

        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.set_builder_keycs(key, value, mode)

        if not isinstance(value, CellBuilder):
            raise ValueError(f"CellBuilder needed")

        self.dict.set_builder_str(str(key), value.builder, mode, 0, signed)
        return self

    def lookup_keycs(self, key: CellSlice) -> Union[CellSlice, DataWithExtra]:
        cs = CellSlice(self.dict.lookup_keycs(key.cell_slice, 0))
        if self.is_augmented:
            return DataWithExtra(cs, self.aug)
        else:
            return cs

    def lookup(self, key: Union[int, CellSlice], signed: bool = None) -> Union[CellSlice, DataWithExtra]:
        """
        Fetch CellSlice stored in ``key``  |br|

        :param key: Integer to be loaded as ``self.key_len`` bit and used as key to search
        :param signed: Signed
        :return: CellSlice that stored by key
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.lookup_keycs(key)

        cs = CellSlice(self.dict.lookup_str(str(key), 0, signed))
        if self.is_augmented:
            return DataWithExtra(cs, self.aug)
        else:
            return cs

    def lookup_delete_keycs(self, key: CellSlice) -> Union[CellSlice, DataWithExtra]:
        cs = CellSlice(self.dict.lookup_keycs_delete(key.cell_slice, 0))
        if self.is_augmented:
            return DataWithExtra(cs, self.aug)
        else:
            return cs

    def lookup_delete(self, key: Union[int, CellSlice], signed: bool = None) -> Union[CellSlice, DataWithExtra]:
        """
        Same as lookup, but delete ``(key, value)`` from VmDict  |br|

        :param key: Integer to be loaded as ``self.key_len`` bit and used as key to search
        :param signed: Signed
        :return: CellSlice that stored by key
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.lookup_delete_keycs(key)

        cs = CellSlice(self.dict.lookup_delete_str(str(key), 0, signed))
        if self.is_augmented:
            return DataWithExtra(cs, self.aug)
        else:
            return cs

    def lookup_ref_keycs(self, key: CellSlice) -> Cell:
        return Cell(self.dict.lookup_keycs_ref(key.cell_slice, 0))

    def lookup_ref(self, key: Union[int, CellSlice], signed: bool = None) -> Cell:
        """
        Same as lookup, but fetch ref stored by ``set_ref``  |br|

        :param key:  Integer to be loaded as ``self.key_len`` bit and used as key to search
        :param signed: Signed
        :return: Cell that stored by key
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.lookup_ref_keycs(key)

        return Cell(self.dict.lookup_ref_str(str(key), 0, signed))

    def lookup_delete_ref_keycs(self, key: CellSlice) -> Cell:
        return Cell(self.dict.lookup_keycs_delete_ref(key.cell_slice, 0))


    def lookup_delete_ref(self, key: Union[int, CellSlice], signed: bool = None) -> Cell:
        """
        Same as ```lookup_delete`` but delete the ref stored by ``set_ref``  |br|

        :param key:  Integer to be loaded as ``self.key_len`` bit and used as key to search
        :param signed: Signed
        :return: Cell that stored by key
        """
        if isinstance(key, int):
            test_value_len(key, self.key_len)
            signed = self._process_sgnd(key, signed)

            if (self.signed and self.key_len > 256) or self.key_len > 257:
                key = CellBuilder().store_bitstring(bin(key)[2:].zfill(self.key_len)).end_cell().begin_parse()

        if isinstance(key, CellSlice):
            return self.lookup_delete_ref_keycs(key)

        return Cell(self.dict.lookup_delete_ref_str(str(key), 0, signed))

    def get_iter(self, direction=False) -> Iterable[tuple[int, CellSlice]]:
        """Simple dict iterator"""

        if (self.signed and self.key_len > 256) or self.key_len > 257:
            raise NotImplementedError("Use .map instead")

        key, value = self.get_minmax_key(direction)
        yield key, value

        while True:
            try:
                key, value = self.lookup_nearest_key(key, not direction)
                yield key, value
            except RuntimeError:
                return

    def map(self, f: Callable[["CellSlice", "CellSlice"], bool]):
        """Map over all key & values of dictionary."""

        tmp_f = lambda key, value: f(CellSlice(key), CellSlice(value))
        self.dict.map(tmp_f)

    def combine_with(self, dict2: "VmDict"):
        """Combine two dictionaries"""

        self.dict.combine_with(dict2.dict)

    def __setitem__(self, key: Union[int, str, CellSlice], value: Union[Union[Union[str, CellSlice], Cell], CellBuilder]):
        if isinstance(key, str):
            key = convert_str_to_int(key)

        test_value_len(key, self.key_len)
        self._process_sgnd(key, None)

        if isinstance(value, str):
            self.set(key, CellSlice(value))
        elif isinstance(value, CellSlice):
            self.set(key, value)
        elif isinstance(value, Cell):
            self.set_ref(key, value)
        elif isinstance(value, CellBuilder):
            self.set_builder(key, value)

    def __getitem__(self, key: Union[int, str, CellSlice]):
        if isinstance(key, str):
            key = convert_str_to_int(key)

        test_value_len(key, self.key_len)
        self._process_sgnd(key, None)

        return self.lookup(key)

    def __repr__(self):
        return self.dict.__repr__()

    def __iter__(self):
        return self.get_iter(False)

    def __reversed__(self):
        return self.get_iter(True)


class TypedVmDict(VmDict):
    def __init__(self, tlb_type: Union[Tuple[TLB, TLB], TLB],
                 key_len: int,
                 signed: bool = False,
                 cell_root: Union[Union[str, Cell], CellSlice] = None,
                 aug: TypedAugmentedData = None,
                 rec_unpack: bool = False):

        self.rec_unpack = rec_unpack

        if isinstance(tlb_type, list) or isinstance(tlb_type, tuple):
            self.value_type = tlb_type[0]
            self.extra_type = tlb_type[1]

            if cell_root:
                csr = cell_root.begin_parse()
                is_empty = not csr.load_bool()
                self.total_extra = self.extra_type.fetch(csr)

                if is_empty:
                    cell_root = None
                else:
                    cell_root = csr.load_ref()

            if aug is None:
                aug = TypedAugmentedData(self.value_type, self.extra_type)

        else:
            self.value_type = tlb_type
            self.extra_type = None

        super().__init__(key_len, signed, cell_root, aug)

    def lookup(self, key: int, signed: bool = None) -> Union[CellSlice, TypedDataWithExtra]:
        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        cs = CellSlice(self.dict.lookup_str(str(key), 0, signed))
        if self.is_augmented:
            return TypedDataWithExtra(cs, self.aug, rec_unpack=self.rec_unpack)
        else:
            return self.value_type.fetch(cs, rec_unpack=self.rec_unpack)

    def get_minmax_key(self, fetch_max: bool = True, invert_first: bool = True, signed: bool = None) -> tuple[
        int, Union[CellSlice, TypedDataWithExtra]]:
        signed = self._process_sgnd(signed=signed)

        key, value = self.dict.get_minmax_key(fetch_max, invert_first, 0, signed)
        cs = CellSlice(value)

        if self.is_augmented:
            return int(key), TypedDataWithExtra(cs, self.aug, rec_unpack=self.rec_unpack)
        else:
            return int(key), self.value_type.fetch(cs, rec_unpack=self.rec_unpack)

    def lookup_nearest_key(self, key: int, fetch_next: bool = True, allow_eq: bool = False,
                           invert_first: bool = True, signed: bool = None) -> tuple[
        int, Union[CellSlice, DataWithExtra]]:
        test_value_len(key, self.key_len)
        signed = self._process_sgnd(key, signed)

        key, value = self.dict.lookup_nearest_key(str(key), fetch_next, allow_eq, invert_first, 0, signed)
        cs = CellSlice(value)

        if self.is_augmented:
            return int(key), TypedDataWithExtra(cs, self.aug, rec_unpack=self.rec_unpack)
        else:
            return int(key), self.value_type.fetch(cs, rec_unpack=self.rec_unpack)
