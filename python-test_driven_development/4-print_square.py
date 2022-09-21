#!/usr/bin/python3
def print_square(size):
    if type(size) == float:
        size = int(size)
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size mus be >= 0")
    if size == 0:
        print()
    else:
        for i in range(size):
            print('#' * size)
