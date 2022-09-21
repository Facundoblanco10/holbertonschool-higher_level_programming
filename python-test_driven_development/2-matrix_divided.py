#!/usr/bin/python3
"""Module"""


def matrix_divided(matrix, div):
    """Function"""
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if type(div) == float:
        div = int(div)
    if type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for idx, row in enumerate(matrix):
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if idx == 0:
            temp = row
        else:
            if len(temp) != len(row):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
        m_list = []
        for i in row:
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            m_list.append(round(i / div, 2))
        new_matrix.append(m_list)
    return (new_matrix)
