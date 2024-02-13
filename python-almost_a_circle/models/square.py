#!/usr/bin/python3

""" This module provides square class.
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Attributes:
        size (int): The side length of the square.
        x (int): X-coordinate of the square's position.
        y (int): Y-coordinate of the square's position.
        id: An optional identifier for the square.
    """

    ATTR_NAMES = {
        "ID": "id",
        "SIZE": "size",
        "X": 'x',
        "Y": 'y'
    }

    def __init__(self, size: int, x: int = 0, y: int = 0, id: int = None):
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self) -> str:
        return "[{}] ({}) {}/{} - {}".format(
            __class__.__name__, self.id, self.x,
            self.y, self.height)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ATTR_NAMES = {
            "ID": "id",
            "SIZE": "size",
            "X": 'x',
            "Y": 'y'
        }
        if len(args):
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif len(kwargs.keys()):
            for key, val in kwargs.items():
                if key == ATTR_NAMES["ID"]:
                    self.id = val
                elif key == ATTR_NAMES["X"]:
                    self.x = val
                elif key == ATTR_NAMES["Y"]:
                    self.y = val
                elif key == ATTR_NAMES["SIZE"]:
                    self.size = val

    def to_dictionary(self):
        temp_dict = {}
        for i in Square.ATTR_NAMES.values():
            temp_dict[i] = getattr(self, i)
        return temp_dict
