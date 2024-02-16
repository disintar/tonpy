# Copyright (c) 2023 Disintar LLP Licensed under the Apache License Version 2.0

import struct
import socket


def ip2int(addr: str):
    return struct.unpack("!i", socket.inet_aton(addr))[0]
