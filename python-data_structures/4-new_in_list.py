#!/usr/bin/python3
from copy import copy
from hashlib import new
from re import M


def new_in_list(my_list, idx, element):
    if idx < 0:
        new_list = my_list
        return (new_list)
    if idx > len(my_list) - 1:
        new_list = my_list
        return (new_list)
    new_list = copy(my_list)
    new_list[idx] = element
    return (new_list)
