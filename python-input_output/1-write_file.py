#!/usr/bin/python3
"""Module"""


def write_file(filename="", text=""):
    """Function"""
    with open(filename, "w") as f:
        char_written = f.write(text)
        return(char_written)