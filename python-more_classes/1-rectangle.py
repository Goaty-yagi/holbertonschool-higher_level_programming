#!/usr/bin/python3

"""
This module defines a basic Rectangle class.
Classes:
    - Rectangle: A class representing a rectangle.
"""


class Rectangle:
    """
    Rectangle Class

    A basic representation of a rectangle with width and height attributes.

    Attributes:
        - ATTRIBUTES_NAME (dict): A dictionary mapping attribute names to
        their string representations.

    Methods:
        - __init__(self, width: int = 0, height: int = 0) ->
        None: Constructor to initialize the rectangle's width and height.
        - attributes_setter(self, value: int, name: str) ->
        int: Helper method to set and validate attribute values.
        - width(self) ->
        int: Getter method for the rectangle's width attribute.
        - width(self, value: int) ->
        None: Setter method for the rectangle's width attribute.
        - height(self) ->
        int: Getter method for the rectangle's height attribute.
        - height(self, value: int) ->
        None: Setter method for the rectangle's height attribute.
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
        if isinstance(value, int):
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
            if name == Rectangle.ATTRIBUTES_NAME["WIDTH"]:
                self.__width = value
            else:
                self.__height = value
            return value
        else:
            raise TypeError("{} must be an integer".format(name))

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int):
        self.attributes_setter(value, "width")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.attributes_setter(value, "height")
