#!/usr/bin/python3
def max_integer(my_list=()):
    max = my_list[0]

    if my_list is None or len(my_list) == 0:
        return (None)
    for n in my_list:
        if max < n:
            max = n
    return (max)
