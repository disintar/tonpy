# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import parse_token_data as parse_token_data_cell

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tonpy import Cell


def parse_token_data(cell: "Cell"):
    return parse_token_data_cell(cell.cell)
