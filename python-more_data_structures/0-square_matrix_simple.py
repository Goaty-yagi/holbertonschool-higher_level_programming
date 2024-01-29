#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    inner_list = []

    for values in matrix:
        for n in values:
            inner_list.append(n ** 2)
        new_matrix.append(inner_list)
        inner_list = []

    return new_matrix
