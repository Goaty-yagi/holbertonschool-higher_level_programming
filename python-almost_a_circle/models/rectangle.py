#!/usr/bin/python3

""" This module proivides Rectangle class inherited from Base class.
"""

from .base import Base


def validator(**kwargs: dict) -> None:
    for key, val in kwargs.items():
        if type(val) != int:
            raise TypeError(
                "{} must be an integer".format(key))
        if key in ("width", "height") and val <= 0:
            raise ValueError("{} must be > 0".format(key))
        if key in ('x', 'y') and val < 0:
            raise ValueError("{} must be >= 0".format(key))


class Rectangle(Base):
    """
    This class inherits Base class, and create
    an instance representing rectangle.

    Constructor(self, width: int, height: int, x: int = 0,
    y: int = 0, id: int = None) -> None):
        create an instance representing rectangle.

    Methods:
        - width: this is property to return and set __width attribute.
        - height: this is property to return and set __height attribute.
        - x: this is property to return and set __x attribute.
        - y: this is property to return and set __y attribute.
    """

    def __init__(self, width: int, height: int, x: int = 0,
                 y: int = 0, id: int = None) -> None:
        validator(**{"width": width, "height": height, 'x': x, 'y': y})
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        validator(**{"width": value})
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        validator(**{"height": value})
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int) -> None:
        validator(**{'x': value})
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int) -> None:
        validator(**{'y': value})
        self.__y = value
