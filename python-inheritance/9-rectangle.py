#!/usr/bin/python3

"""
This module provides Rectangle class
"""
import importlib
BaseGeometry = importlib.import_module("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry class.

    Methods:
    - init(self, width: int, height: int): create a new instance.
    - __str__(self) -> str: return [Rectangle] self.__width, self.__height
    - area(self) -> int: return area of rectangle
    - integer_validator(self, name: str, value: int): valid args
    """

    ATTR_NAMES = {
        "WIDTH": "width",
        "HEIGHT": "height"
    }

    def __init__(self, width: int, height: int) -> None:
        self.__width = self.integer_validator(
            Rectangle.ATTR_NAMES["WIDTH"], width)
        self.__height = self.integer_validator(
            Rectangle.ATTR_NAMES["HEIGHT"], height)

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self) -> int:
        return self.__width * self.__height

    def integer_validator(self, name: str, value: int) -> int:
        super().integer_validator(name, value)
        return value
