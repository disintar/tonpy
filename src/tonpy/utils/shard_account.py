# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.types import begin_cell


def get_empty_shard_account():
    return begin_cell() \
        .store_ref(begin_cell().store_uint(0, 1).end_cell()) \
        .store_uint(0, 256) \
        .store_uint(0, 64) \
        .end_cell()
