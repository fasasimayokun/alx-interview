#!/usr/bin/python3

"""0-lockboxes.py function"""


def canUnlockAll(boxes):
    """a func that determines if all the boxes can be opened"""
    nm = len(boxes)
    unlocked = set([0])
    keys = boxes[0]
    lifo = list(keys)
    while lifo:
        key = lifo.pop()
        if key < nm and key not in unlocked:
            unlocked.add(key)
            lifo.extend(boxes[key])
    return len(unlocked) == nm
