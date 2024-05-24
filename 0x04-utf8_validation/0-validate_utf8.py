#!/usr/bin/python3
"""a py script for UTF-8 Validation"""


def validUTF8(data):
    """
    a func that determines if a given dataset represents valid UTF-8 encoding
    """
    def num_of_bytes(n):
        """
        a func that gets the plage number of a number in UTF-8
        """
        msk = 1 << 7
        nm = 0
        while (n & msk):
            nm += 1
            msk = msk >> 1
        return nm

    count = 0
    for nm in data:
        if not count:
            count = num_of_bytes(nm)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if num_of_bytes(nm) != 1:
                return False
    return count == 0
