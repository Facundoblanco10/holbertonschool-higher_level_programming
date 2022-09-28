#!/usr/bin/python3
"""Module"""


import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not os.path.exists(filename):
    save_to_json_file(sys.argv[1:], filename)
    exit()
try:
    p_list = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        p_list.append(sys.argv[i])
    save_to_json_file(p_list, filename)
except Exception:
    Exception
