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