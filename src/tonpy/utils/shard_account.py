# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.types import begin_cell, Cell
import json
from tonpy.libs.python_ton import shard_is_ancestor, shard_child, shard_parent
from tonpy.libs.python_ton import parse_shard_account as cparse_shard_account


def parse_shard_account(cell: Cell):
    return json.loads(cparse_shard_account(cell.cell))


def get_empty_shard_account():
    return begin_cell() \
        .store_ref(begin_cell().store_uint(0, 1).end_cell()) \
        .store_uint(0, 256) \
        .store_uint(0, 64) \
        .end_cell()
