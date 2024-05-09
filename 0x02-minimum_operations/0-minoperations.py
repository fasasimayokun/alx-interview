#!/usr/bin/python3
"""module for 0-minoperations.py"""


def minOperations(n):
    """
    a func that calculates the fewest number
    of operations needed to
    result in exactly n H characters in the file
    """
    min_op = 0
    dv = 2
    while (isinstance(n, int) and n > 1):
        while (n % dv):
            dv += 1
        min_op += dv
        n = n // dv
    return min_op
