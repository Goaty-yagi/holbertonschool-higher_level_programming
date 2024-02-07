#!/usr/bin/python3

"""
This module provides Square class
"""
import importlib
Rectangle = importlib.import_module("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class inherits from Square class.

    Methods:
    - init(self, width: int, height: int): create a new instance.
    - __str__(self) -> str: return [Rectangle] self.__width, self.__height
    - area(self) -> int: return area of rectangle
    - integer_validator(self, name: str, value: int): valid args
    """

    Rectangle.ATTR_NAMES["SIZE"] = "size"

    def __init__(self, size: int) -> None:
        super().__init__(size, size)
        self.__size = self.integer_validator(
            Square.ATTR_NAMES["SIZE"], size)

    def area(self) -> int:
        return self.__size ** 2

    def integer_validator(self, name: str, value: int) -> int:
        super().integer_validator(name, value)
        return value
