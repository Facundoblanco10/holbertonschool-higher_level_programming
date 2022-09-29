#!/usr/bin/python3
"""PASCAL TRIANGLE"""


def pascal_triangle(n):
    p_list = []
    row = [1]
    if n <= 0:
        return p_list
    
    for i in range(n):
        new_list = [1]
        for idx in range(i):
            if idx + 1 < len(row):
                new_list.append(row[idx] + row[idx + 1])
            else:
                new_list.append(1)
                row = list(new_list)
        p_list.append(new_list)
    return p_list
