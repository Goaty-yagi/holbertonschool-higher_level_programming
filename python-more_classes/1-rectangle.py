#!/usr/bin/python3

"""
This module defines a basic Rectangle class.
"""


class Rectangle:
    """
    Rectangle Class

    A basic representation of a rectangle.
    """
    ATTRIBUTES_NAME = {
        "WIDTH": "width",
        "HEIGHT": "height"
    }

    def __init__(self, width: int = 0, height: int = 0) -> None:
        self.__height = self.attributes_setter(
            height, Rectangle.ATTRIBUTES_NAME["HEIGHT"])

        self.__width = self.attributes_setter(
            width, Rectangle.ATTRIBUTES_NAME["WIDTH"])

    def attributes_setter(self, value: int, name: str) -> int:
        if isinstance(value, int) and not value < 0:
            if name == Rectangle.ATTRIBUTES_NAME["WIDTH"]:
                self.__width = value
            else:
                self.__height = value
            return value
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))
        else:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: int):
        return self.attributes_setter(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        return self.attributes_setter(value, "height")
