#!/usr/bin/python3
"""Module"""


def print_square(size):
    """Function"""
    if size == 0:
        return
    if type(size) == float:
        size = int(size)
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
