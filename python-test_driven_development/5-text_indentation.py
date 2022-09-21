#!/usr/bin/python3
"""Module"""


def text_indentation(text):
    """Function"""
    if type(text) != str:
        raise TypeError("text must be a string")
    punctuation = False
    for ch in text:
        if punctuation:
            if ch == " ":
                continue
            punctuation = False
        print(f"{ch}", end='')
        if ch == '.' or ch == '?' or ch == ':':
            print('\n')
            punctuation = True
        