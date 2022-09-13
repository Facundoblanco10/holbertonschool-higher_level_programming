#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, item in enumerate(row):
            print("{}".format(item), end='')
            if idx != len(row) - 1:
                print(' ', end='')
        print()
