#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    b = 0

    if len(tuple_a) != 0:
        for idx, n in enumerate(tuple_a):
            if idx == 0:
                a = n
            if idx == 1:
                b = n
    if len(tuple_b) != 0:
        for idx, n in enumerate(tuple_b):
            if idx == 0:
                a += n
            if idx == 1:
                b += n
    return (a, b)
