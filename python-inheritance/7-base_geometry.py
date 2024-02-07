#!/usr/bin/python3
"""
This module provides a class BaseGeometory
"""


class BaseGeometry:
    """
    This class makes BaseGeometory object.

    Methods:
    - area(self): raise Exception
    - integer_validator(self, name: str, value: int): raise Exceptions
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name: str, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
