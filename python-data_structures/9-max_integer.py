#!/usr/bin/python3
from re import M


def max_integer(my_list=()):

    if my_list is None or len(my_list) == 0:
        return (None)
    max = my_list[0]
    for n in my_list:
        if max < n:
            max = n
    return (max)
