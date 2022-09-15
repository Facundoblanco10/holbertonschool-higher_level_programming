#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = []
    for key in a_dictionary:
        sort_keys.append(key)
    sort_keys.sort()
    for key in sort_keys:
        print(f"{key}: {a_dictionary[key]}")
