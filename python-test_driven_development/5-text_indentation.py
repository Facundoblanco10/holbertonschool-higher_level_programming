#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for ch in text:
        print(f"{ch}", end='')
        if ch == '.' or ch == '?' or ch == ':':
            print('\n')
