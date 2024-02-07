#!/usr/bin/python3
"""
This module provides a functuin is_same_class
"""


def is_same_class(obj, a_class):
    """
    This function checks if obj is an instance of a_class.

    Parameter:
    - obj(type:any): The obj to be chacked.
    - a_class: The class to check against.

    Return:
    - True is obj is instance of a_class while False if not.
    """
    return obj.__class__ == a_class
