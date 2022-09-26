#!/usr/bin/python3

def lookup(obj):
    my_list = []
    for i in dir(obj):
        my_list.append(i)
    return (my_list)
