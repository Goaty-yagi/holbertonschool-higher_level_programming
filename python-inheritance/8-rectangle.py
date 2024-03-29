#!/usr/bin/python3

"""
This module provides Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


ATTR_NAMES = {
    "WIDTH": "width",
    "HEIGHT": "height"
}


class Rectangle(BaseGeometry):
    """
    This class inherits from BaseGeometry class.

    Methods:
    - init(self, width: int, height: int): create a new instance.
    - integer_validator(self, name: str, value: int): valid args
    """

    def __init__(self, width: int, height: int) -> None:
        self.__width = self.integer_validator(
            ATTR_NAMES["WIDTH"], width)
        self.__height = self.integer_validator(
            ATTR_NAMES["HEIGHT"], height)

    def integer_validator(self, name: str, value: int) -> int:
        super().integer_validator(name, value)
        return value
