#!/usr/bin/python3
"""Module"""


def text_indentation(text):
    """Function"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for ch in text:
        print(f"{ch}", end='')
        if ch == '.' or ch == '?' or ch == ':':
            print('\n')
