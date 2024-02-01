"""
Module: math_operations

This module provides add operation.

Functions:
    - add_integer(a, b=98): Adds two integers or
    floats and returns the result as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number
        to be added. Defaults to 98.

    Returns:
        int: The sum of the two numbers, returned as an integer.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
