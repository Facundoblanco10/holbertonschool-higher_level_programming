#!/usr/bin/python3
"""Module"""


import json


def load_from_json_file(filename):
    """Function"""
    with open(filename, "x") as f:
        return json.load(f)
