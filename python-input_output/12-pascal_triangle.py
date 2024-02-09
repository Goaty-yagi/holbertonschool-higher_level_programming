#!/usr/bin/python3

""" This module provides pascal_triangle function.
"""


def pascal_triangle(n: int) -> list:
    """ This function make pascal_triangle matrix, and return it.

    Args:
        n (int): n representing level of pascal_triangle.

    Returns:
        list: lists in list representing pascal_triangle
    """
    matrix = []
    inner_list = []
    for i in range(n):
        try:
            if len(matrix):
                for n in range(len(matrix[i - 1])):
                    inner_list.append(
                        matrix[i - 1][n] + matrix[i - 1][n - 1]
                        if n != 0 else matrix[i - 1][n])
        except IndexError:
            pass
        finally:
            inner_list.append(1)
            matrix.append(inner_list)
            inner_list = []

    return matrix
