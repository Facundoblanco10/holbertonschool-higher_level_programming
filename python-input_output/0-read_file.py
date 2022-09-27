#!/usr/bin/python3
"""Module"""


def read_file(filename=""):
    with open(filename, encoding="UTF8") as f:
        read_data = f.read()
        print(read_data)
        f.closed