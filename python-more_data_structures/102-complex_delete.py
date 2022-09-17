#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary):
        if a_dictionary[i] == value:
            a_dictionary.pop(i, value)
    return (a_dictionary)
