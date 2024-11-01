#!/usr/bin/python3
"""
thi is module
"""


def validUTF8(data):
    """
    this is utf-8 validation
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF
        if num_bytes == 0:
            if (byte & mask1) == 0:
                num_bytes = 0
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == (mask1 >> 1):
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == (mask1 >> 2):
                num_bytes = 3
            else:
                return False
        else:
            if (byte & mask1) != mask1 or (byte & mask2) != 0:
                return False
            num_bytes -= 1
    return num_bytes == 0
