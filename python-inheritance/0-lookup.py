#!/usr/bin/python3
"""Module"""


def lookup(obj):
    """function"""
    my_list = []
    for i in dir(obj):
        my_list.append(i)
    return (my_list)
