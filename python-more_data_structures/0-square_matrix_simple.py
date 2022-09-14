#!/usr/bin/python3
from re import L
from sqlite3 import Row


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        temp = []
        for i in row:
            temp.append(i * i)
        new_matrix.append(temp)
    return (new_matrix)
