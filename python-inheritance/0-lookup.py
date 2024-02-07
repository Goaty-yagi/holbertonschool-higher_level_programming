#!/usr/bin/python3

"""
This module provides a function to look up and retrieve the attributes
and methods associated with a given object.

Functions:
- lookup(obj): Returns a list of attributes and methods
associated with the object.
"""


def lookup(obj: object) -> list:
    """
    Return a list of attributes and methods associated with the object.

    Parameters:
        Any object for which the attributes and methods to be looked up.

    Return:
        A list of attributes and methods associated with the given object.
    """
    return dir(obj)
