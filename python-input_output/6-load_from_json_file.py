#!/usr/bin/python3
"""Module"""


import json


def load_from_json_file(filename):
    """Function"""
    x = json.loads(filename)
    with open(x, "x") as f:
        return f
