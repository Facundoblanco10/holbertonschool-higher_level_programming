#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    max = []
    for k in a_dictionary:
        if len(max) == 0:
            max = k
        if a_dictionary[max] < a_dictionary[k]:
            max = k
    return (max)