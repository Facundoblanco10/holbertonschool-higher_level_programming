#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, "a") as f:
        char_num = f.write(text)
        return char_num
