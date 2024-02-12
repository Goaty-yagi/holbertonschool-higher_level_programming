#!/usr/bin/python3

""" This module provides Base class
"""


class Base:
    """
    This class representing base class
    """
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
