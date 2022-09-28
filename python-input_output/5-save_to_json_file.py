#!/usr/bin/python3
"""Module"""


import json


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, "a") as f:
        f.write(json.dumps(my_obj))
