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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = 0
        self.__position = (0, 0)
        self.setter(size)
        self.position_setter(position)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        return self.setter(value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        return self.position_setter(value)

    def position_setter(self, new_value):
        if isinstance(new_value, tuple) and len(new_value) == 2:
            if all(value >= 0 for value in new_value):
                self.__position = new_value
                return
        raise TypeError("position must be a tuple of 2 positive integers")

    def setter(self, new_value):
        if isinstance(new_value, int):
            if new_value < 0:
                raise ValueError("size must be >= 0")
            self.__size = new_value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for k in range(self.__size):
                print("#", end="")
            print()

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
