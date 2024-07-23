#!/usr/bin/python3
""" the UTF-8 Validation"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    byte_ct = 0

    for d in data:
        if byte_ct == 0:
            if d >> 5 == 0b110 or d >> 5 == 0b1110:
                byte_ct = 1
            elif d >> 4 == 0b1110:
                byte_ct = 2
            elif d >> 3 == 0b11110:
                byte_ct = 3
            elif d >> 7 == 0b1:
                return False
        else:
            if d >> 6 != 0b10:
                return False
            byte_ct -= 1
    return byte_ct == 0
