#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if islower(i):
            i = chr(ord(i) - 32)
        print("{0}".format(i), end='')
    print("")


def islower(c):
    if ord(c) in range(97, 123):
        return (True)
    else:
        return (False)
