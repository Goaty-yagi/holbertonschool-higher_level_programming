#!/usr/bin/python3

""""
This module provides add operation.

Usage:
    __import__('0-add_integer').add_integer

    add_integer(1, 2)
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

    Raises:
            ValueError: If a or b is not int or float.
    """
    if not isinstance(a, (int, float)):
        raise ValueError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise ValueError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
