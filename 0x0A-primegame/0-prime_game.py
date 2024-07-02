#!/usr/bin/python3
"""a py script for 0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """
    this func returns the name of the player that won
    the most rounds if no winner it returns None
    x is the number of rounds and nums is an array of n
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for nm in range(2, len(a)):
        rdm_multiples(a, nm)

    for nm in nums:
        if sum(a[0:nm + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rdm_multiples(lis, x):
    """this func removes multiple of primes"""
    for nm in range(2, len(lis)):
        try:
            lis[nm * x] = 0
        except (ValueError, IndexError):
            break
