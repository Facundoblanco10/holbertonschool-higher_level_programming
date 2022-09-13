#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [None] * len(my_list)
    for idx, n in enumerate(my_list):
        # if is is 0 is true else, is false
        new_list[idx] = n % 2 == 0
    return (new_list)
