#!/usr/bin/python3

"""
Module: matrix_operations

Provides a function for dividing all elements of a matrix by a divisor.

Function:
    - matrix_divided(matrix, div): Divides all elements of
    a matrix by a divisor and returns the result.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns the result.

    Parameters:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list of lists: The resulting matrix after division.

    Raises:
        TypeError: If `div` is not a number, if `matrix` is not a
        list of lists of integers/floats, or if any element of
        `matrix` is not an integer.
        ZeroDivisionError: If `div` is zero.
        TypeError: If any row of `matrix` does not have the same size.
    """

    inner_list_length = 0
    new_matrix = []
    list_error_text = (
        "matrix must be a matrix (list of lists) "
        "of integers/floats"
    )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(list_error_text)
    if not all(isinstance(each, list) for each in matrix):
        raise TypeError(list_error_text)

    if len(matrix):
        inner_list_length = len(matrix[0])

    for each in matrix:
        if not all(isinstance(val, int) for val in each):
            raise TypeError(list_error_text)
        if not len(each) == inner_list_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append(list(round(val / div, 2) for val in each))
    return (new_matrix)
