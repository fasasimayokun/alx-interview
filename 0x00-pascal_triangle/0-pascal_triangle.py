#!/usr/bin/python3
"""
A func that returns a list of lists of ints
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a list of lists of ints representing the Pascal's triangle of n

    Attributes:
        n (any): int

    Returns:
        - An empty list if n <= 0
        - A list of lists of integers if n >= 0
    """
    if (n <= 0):
        return ([])
    result = list([] for _ in range(n))
    for i in range(0, n):
        temp = res[i]
        temp.append(1)
        counter = 0 if (i == 0) else len(res[i - 1])
        for p in range(0, counter):
            if (p + 1 < len(res[i - 1])):
                a = res[i - 1][p]
                b = res[i - 1][p + 1]
                temp.append(sum([a, b]))
            else:
                temp.append(1)
        res[i] = temp
    return (res)
