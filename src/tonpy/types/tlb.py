from collections import defaultdict
from enum import Enum
from typing import Optional

from tonpy.types import CellSlice, CellBuilder, Cell


class RecordBase:
    """
    Each TLB type have ``Record`` subclass means instance of TLB type |br|
    If you have multiple constructors name of ``Record`` class will be change to ``Record_{{constructor_name}}`` |br|
    Each record have ``__init__`` function witch contains all fields of TLB type |br|
    Check out ``test_tlb.py`` ``test_records`` function
    """

    def get_tag_enum(self):
        """"""
        raise NotImplementedError

    def get_tag(self):
        """"""
        raise NotImplementedError

    def get_tag_len(self):
        """"""
        raise NotImplementedError

    def get_type_class(self):
        """"""
        raise NotImplementedError

    def unpack(self, cs: CellSlice) -> bool:
        """"""
        raise NotImplementedError

    def cell_unpack(self, cell_ref: Cell) -> bool:
        """"""
        raise NotImplementedError


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

    cons_len = None
    cons_tag = None
    tag_to_class = {}

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
        Store enum from ``self.cons_tag`` on position ``value`` (if ``TLB.Tag`` not constant) to `cb: CellBuilder` |br|
        If ``self.const_tag`` is exact (tags are matched positions in lexicographic order) then will store ``value`` |br|
        If ``value is None`` and ``TLB.Tag is constant`` will store constant ``TLB.Tag`` else will raise an error |br|

        :param cb: CellBuilder to store enum to
        :param value: Value or enum position to store enum from
        :return: True
        """
        raise NotImplementedError

    def always_special(self) -> bool:
        """Is current type marked as special cell or not"""

        raise NotImplementedError

    def unpack(self, cs: CellSlice) -> Optional[RecordBase]:
        """
        Unpack current TLB and return TLB.Record if success, else return None

        :param cs: CellSlice to unpack TLB from
        :return: TLB.Record instance or None
        """

        try:
            t = self.tag_to_class[self.get_tag(cs)]()

            if not t.unpack(cs):
                return None

            return t
        except (RuntimeError, KeyError, ValueError):
            return None

    def cell_unpack(self, cell_ref: Cell) -> Optional[RecordBase]:
        """
        Same as ``unpack`` but

        :param cell_ref:
        :return:
        """
        if cell_ref.is_null():
            return None

        cs = cell_ref.begin_parse()

        t = self.unpack(cs)

        if t is not None and not cs.empty_ext():
            return None

        return t


class TLBComplex(TLB):
    def __init__(self):
        super().__init__()
