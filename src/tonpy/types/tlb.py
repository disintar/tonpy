from collections import defaultdict
from enum import Enum
from typing import Optional

from tonpy.types import CellSlice, CellBuilder


class TLB(object):
    class Tag(Enum):
        """
        Contractor tags enums stored as lexicographic order

        .. code-block::

            a$0 = A;
            b$10 = A;
            c$1 = A;

        Means:

        .. code-block:: Python

            class Tag(Enum):
               a = 0
               b = 1
               c = 2

            cons_len = [1, 2, 1]
            cons_tag = [0, 2, 1]
        """

        raise NotImplemented

    cons_len = None
    cons_tag = None

    def get_tag(self, cs: CellSlice) -> Optional["TLB.Tag"]:
        """
        Fetch tag from CellSlice ``cs`` and return ``TLB.Tag`` enum

        :param cs: CellSlice to fetch tag from
        :return: ``TLB.Tag`` enum
        """
        raise NotImplemented

    def fetch_enum(self, cs: CellSlice) -> int:
        """
        Fetch enum tag value from ``CellSlice`` of type ``TLB``

        :param cs: CellSlice to fetch enum tag value from
        :return: Enum tag value of type ``TLB`` store in ``cs: CellSlice``
        """

        raise NotImplementedError

    def store_enum_from(self, cb: CellBuilder, value: int = None) -> bool:
        """
        Store enum from ``self.cons_tag`` on position ``value`` (if ``TLB.Tag`` not constant) to `cb: CellBuilder`
        If ``self.const_tag`` is exact (tags are matched positions in lexicographic order) then will store ``value``
        If ``value is None`` and ``TLB.Tag is constant`` will store constant ``TLB.Tag`` else will raise an error

        :param cb: CellBuilder to store enum to
        :param value: Value or enum position to store enum from
        :return: True
        """
        raise NotImplementedError


class TLBComplex(object):
    pass
