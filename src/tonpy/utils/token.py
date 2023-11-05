# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from tonpy.libs.python_ton import parse_chunked_data
from tonpy.types.vmdict import VmDict
from hashlib import sha256
from tonpy import CellSlice, Cell


def parse_token_d_value(value):
    if value.bits > 0:
        value_type = value.load_uint(8)
    else:
        value_type = -1
    if value_type == 0:
        try:
            return {
                'type': 'snake',
                'value': value.load_string()
            }
        except Exception as e:
            return {
                'type': 'unknown',
                'value': ''
            }
    elif value_type == 1:
        return {
            'type': 'chunks',
            'value': parse_chunked_data(value)
        }
    else:
        return {
            'type': 'unknown',
            'value': ''
        }


def parse_token_data(data):
    if isinstance(data, Cell):
        data = data.begin_parse()

    assert isinstance(data, CellSlice)
    if data.bits >= 8:
        ct = data.load_uint(8)
    else:
        ct = -1

    if ct == 0:
        valid_keys = ["uri", "name", "description", "image", "image_data", "symbol",
                      "decimals", "amount_style", "render_type", "jetton", "master", "address"]

        valid_keys_hashed = {}
        for i in valid_keys:
            valid_keys_hashed[sha256(i.encode()).hexdigest().upper()] = i

        data = VmDict(256, False, data.load_ref())

        result = {}

        for i in data:
            key = hex(i[0]).upper()[2:]
            if key in valid_keys_hashed:
                result[valid_keys_hashed[key]] = parse_token_d_value(i[1].load_ref().begin_parse())
            else:
                result[key] = parse_token_d_value(i[1].load_ref().begin_parse())
        return {
            'type': 'onchain',
            'value': result
        }
    elif ct == 1:
        return {
            'type': 'offchain',
            'value': data.load_string()
        }
    else:
        raise ValueError

# def parse_token_data(cell: "Cell"):
#     return parse_token_data_cell(cell.cell)
