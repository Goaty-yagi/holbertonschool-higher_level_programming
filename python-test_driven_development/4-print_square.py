#!/usr/bin/python3

"""
Provides a function for printing a square of a specified size.

Function:
    - print_square(size): Prints a square of the
    specified size using '#' characters.
"""


def print_square(size):
    """
    Prints a square of the specified size using '#' characters.

    Parameters:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
