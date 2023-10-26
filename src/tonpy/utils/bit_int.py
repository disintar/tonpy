# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

def test_value_len(value: int, value_len: int):
    if value < 0:
        value *= -1
    assert len(bin(value)[2:]) <= value_len, f"Value is bigger than {value_len} bits"
