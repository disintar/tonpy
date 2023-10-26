# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

from bitstring import BitArray


def bitstring_to_utf8(bitstring_: str, strict: bool = True) -> str:
    tmp = len(bitstring_) % 8

    if tmp != 0 and strict:
        raise ValueError(f"Final bitstring has {len(bitstring_)} bits, (% 8) check fail")

    if tmp == 0:
        bits = BitArray(bin=bitstring_)
    else:
        bits = BitArray(bin=bitstring_[:-1 * tmp])

    bytes_data = bits.tobytes()

    # Decode bytes to UTF-8 text
    utf8_text = bytes_data.decode("utf-8")

    return utf8_text


def convert_str_to_bitsring(string: str) -> str:
    encoded_bitstring = string.encode('utf-8')
    return ''.join(bin(byte)[2:].zfill(8) for byte in encoded_bitstring)


def convert_str_to_int(string: str) -> int:
    return int(convert_str_to_bitsring(string), 2)


