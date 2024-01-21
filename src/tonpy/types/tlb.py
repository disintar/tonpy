# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from collections import defaultdict
from enum import Enum
from typing import Optional, List, Union, Callable

from tonpy.types import CellSlice, CellBuilder, Cell


def rec_dump(item, dump_bin_as_hex):
    output = {}
    for name in item.field_names:
        value = getattr(item, name)
        if issubclass(type(value), RecordBase):
            output[name] = rec_dump(value, dump_bin_as_hex=dump_bin_as_hex)
        else:
            if dump_bin_as_hex and isinstance(value, str) and len(value) % 8 == 0:
                try:
                    output[name] = hex(int(value, 2)).upper()[2:]
                    continue
                except Exception as e:
                    pass

            output[name] = value
    return output


class RecordBase:
    """
    Each TLB type have ``Record`` subclass means instance of TLB type |br|
    If you have multiple constructors name of ``Record`` class will be change to ``Record_{{constructor_name}}`` |br|
    Each record have ``__init__`` function witch contains all fields of TLB type |br|
    Check out ``test_tlb.py`` ``test_records`` function
    """

    def __init__(self):
        self.field_names = []  # names of all fetched fields
        self.conditional_fields = []  # names of all fields that are conditional
        self.negate_params = []  # params that determinate on serialization process

    def get_tag_enum(self):
        """Get current TLB.Record constructor tag in ``Enum`` type of ``TLB.Tag``"""
        raise NotImplementedError

    def get_tag(self):
        """Get current TLB.Record constructor tag"""
        raise NotImplementedError

    def get_tag_len(self):
        """Get length of bits for current TLB.Record constructor tag"""
        raise NotImplementedError

    def get_type_class(self):
        """Get TLB type of current record"""
        raise NotImplementedError

    def unpack(self, cs: CellSlice, rec_unpack: bool = False,
               strict: bool = True) -> bool:
        """
        Unpack current CellSlice as TLB.Record to fields, if success return True |br|
        All field values store in class object. If ``rec_unpack`` is True - unpack all types with recursion |br|
        Note: simple types that contains only from tags don't need ``rec_unpack``, they will be fetched immediately |br|

        :param cs: CellSlice to be fetched as TLB.Record
        :param rec_unpack: Need to unpack all types with recursion
        :param strict: If False some failed to parse subtypes can be None
        :return: Is unpack was success
        """
        raise NotImplementedError

    def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False,
                    strict: bool = True) -> bool:
        """
        Unpack current Cell as TLB.Record to fields, if success return True |br|
        All field values store in class object. If ``rec_unpack`` is True - unpack all types with recursion |br|
        Note: simple types that contains only from tags don't need ``rec_unpack``, they will be fetched immediately |br|
        If after unpack Cell contains some data - return False |br|

        :param cell_ref: Cell to be fetched as TLB.Record
        :param rec_unpack: Need to unpack all types with recursion
        :param strict: If False some failed to parse subtypes can be None
        :return: Is unpack was success
        """
        raise NotImplementedError

    def pack(self, cb: CellBuilder) -> None:
        raise NotImplementedError

    def cell_pack(self) -> Cell:
        raise NotImplementedError

    def add_r1(self, val: str, y: int, z: int) -> bool:
        if y > z:
            return False

        x = z - y
        setattr(self, val, x)
        return x >= 0

    def mul_r1(self, val: str, y: int, z: int) -> bool:
        if not y or z % y != 0:
            return False

        x = z / y
        setattr(self, val, x)
        return x >= 0

    def store_from(self, cb, value):
        """Recursively pack TLB type to CellBuilder"""
        cb.store_slice_or_tlb(value)

    def dump(self, dump_bin_as_hex=True):
        """Recursively convert TLB to dict"""
        return rec_dump(self, dump_bin_as_hex=dump_bin_as_hex)

    def to_dict(self, rec_unpack=False, convert_cells_to_bocs=False):
        answer = {}

        for field in self.field_names:
            value = getattr(self, field)

            if rec_unpack and issubclass(type(value), RecordBase):
                answer[field] = value.to_dict(rec_unpack=rec_unpack, convert_cells_to_bocs=convert_cells_to_bocs)
            else:
                if convert_cells_to_bocs and isinstance(value, (Cell, CellSlice, CellBuilder)):
                    value = value.to_boc()

                answer[field] = value
        return answer


class TLB(object):
    class Tag(Enum):
        """
        Contractor tags enums stored as lexicographic order |br|

        .. code-block::

            a$0 = A;
            b$10 = A;
            c$1 = A;

        Means: |br|

        .. code-block:: Python

            class Tag(Enum):
               a = 0
               b = 1
               c = 2

            cons_len = [1, 2, 1]
            cons_tag = [0, 2, 1]
        """

        # raise NotImplemented
        pass

    class Record(RecordBase):
        pass

    cons_len: Union[List[int], int] = None
    cons_tag: List[int] = None
    tag_to_class = {}
    original_cell: Optional[Cell] = None
    original_cell_slice: Optional[CellSlice] = None
    params_attrs = []  # all params defined for TLB type from __init__
    has_params = False  # is type is parametrized

    def get_tag(self, cs: CellSlice) -> Optional["TLB.Tag"]:
        """
        Fetch tag from CellSlice ``cs`` and return ``TLB.Tag`` enum |br|
        :param cs: CellSlice to fetch tag from
        :return: ``TLB.Tag`` enum
        """
        raise NotImplemented

    def fetch_enum(self, cs: CellSlice) -> int:
        """
        Fetch enum tag value from ``CellSlice`` of type ``TLB`` |br|

        :param cs: CellSlice to fetch enum tag value from
        :return: Enum tag value of type ``TLB`` store in ``cs: CellSlice``
        """

        raise NotImplementedError

    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        """
        Store enum ``value`` from ``self.cons_tag`` to `cb: CellBuilder` |br|
        If ``self.const_tag`` is exact (tags are matched positions in lexicographic order) then will store ``value`` |br|
        If ``value is None`` and ``TLB.Tag is constant`` will store constant ``TLB.Tag`` else will raise an error |br|

        :param cb: CellBuilder to store enum to
        :param value: Value or enum position to store enum from
        :return: True
        """
        raise NotImplementedError

    def store_from(self, cb, value):
        cb.store_slice_or_tlb(value)

    def always_special(self) -> bool:
        """Is current type marked as special cell or not"""
        return False

    def unpack(self, cs: CellSlice, rec_unpack: bool = False,
               strict: bool = True) -> Optional[RecordBase]:
        """
        Unpack current TLB and return TLB.Record if success, else return None |br|

        By default, rec_unpack is False because for large TLB structures it can be slow. |br|
        More simple way is to skip needed structures one by one and load to python objects only needed ones. |br|


        :param cs: CellSlice to unpack TLB from
        :param rec_unpack: pass to RecordBase ``rec_unpack``
        :param strict: pass to RecordBase ``strict``
        :return: TLB.Record instance or None
        """

        self.original_cell_slice = cs

        try:
            t = self.tag_to_class[self.get_tag(cs)]()

            if not t.unpack(cs, rec_unpack, strict=strict):
                return None

            return t
        except (TabError):
            return None

    def cell_unpack(self, cell_ref: Cell, rec_unpack: bool = False,
                    strict: bool = True) -> Optional[RecordBase]:
        """
        Same as ``unpack`` but

        :param cell_ref:
        :param rec_unpack: pass to RecordBase ``rec_unpack``
        :param strict: pass to RecordBase ``strict``
        :return:
        """
        if cell_ref.is_null():
            return None

        # save original cell
        self.original_cell = cell_ref

        cs = cell_ref.begin_parse()

        t = self.unpack(cs, rec_unpack, strict=strict)

        if t is not None and not cs.empty_ext():
            return None

        return t

    def fetch(self, cell_or_slice: Union[Cell, CellSlice], rec_unpack: bool = False,
              strict: bool = True, **kwargs) -> "Optional[Union[Union[Union[TLB.Record, Cell], CellSlice], None]]":
        """
        :param cell_or_slice:
        :param rec_unpack: pass to RecordBase ``rec_unpack``
        :param strict: pass to RecordBase ``strict``
        :return: Will return cell/cellslice if cell is special, else will return record on success, else None
        """

        if self.always_special():
            return cell_or_slice

        if isinstance(cell_or_slice, Cell):
            return self.cell_unpack(cell_or_slice, rec_unpack, strict=strict)
        elif isinstance(cell_or_slice, CellSlice):
            return self.unpack(cell_or_slice, rec_unpack, strict=strict)
        else:
            raise ValueError(f"Type {type(cell_or_slice)} is not supported")

    def fetch_to(self, to_obj: object,
                 cell_or_slice: Union[Cell, CellSlice],
                 unpack_names: List[str],
                 rec_unpack: bool = False,
                 strict: bool = True):
        """
        Same as fetch, but copy negate params to ``to_obj`` with names from ``unpack_names``

        :param to_obj:
        :param cell_or_slice:
        :param unpack_names:
        :param rec_unpack:
        :param strict:
        :return:
        """

        rec = self.fetch(cell_or_slice=cell_or_slice, rec_unpack=rec_unpack, strict=strict)

        if rec is None:
            return rec

        if not (len(rec.negate_params) == len(unpack_names)):
            return None

        for param, name in zip(rec.negate_params, unpack_names):
            setattr(to_obj, name, getattr(rec, param))

        return rec

    def get_param_record(self, item: str) -> Callable:
        """Copy params from TLB to Record"""
        TMPClass = type("TMPClass", (getattr(self, item),), {})
        TMPClass.name = item

        if self.has_params:
            # copy all params
            for i in set(self.params_attrs):
                if hasattr(self, i):
                    setattr(TMPClass, i, getattr(self, i))

        return TMPClass

    def nat_abs(self, x: int):
        return (x > 1) * 2 + (x & 1)

    def store_ref_or_tlb(self, cb: CellBuilder, value):
        cb.store_ref_or_tlb(value)
