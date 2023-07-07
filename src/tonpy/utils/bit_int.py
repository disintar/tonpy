def test_value_len(value: int, value_len: int):
    if value < 0:
        value *= -1
    assert len(bin(value)[2:]) <= value_len, f"Value is bigger than {value_len} bits"
