#!/usr/bin/python3

"""Module: 0-square.py

This module provides a simple implementation of a Square class.

Classes:
    Square: Represents a square shape.

Usage:
    Square = __import__('0-square').Square

    # Example usage
    square = Square()
"""


class Square:
    """Represents a square shape.

    Attributes:
        None

    Methods:
        None

    Usage:
        from square import Square

        # Create a square object
        square = Square()
    """

    def __init__(self, size=0):
        self.__size = 0
        self.setter(size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        return self.setter(value)

    def setter(self, new_value):
        if isinstance(new_value, int):
            if new_value < 0:
                raise ValueError("size must be >= 0")
            self.__size = new_value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2
