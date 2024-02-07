#!/usr/bin/python3

"""
This module provides is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """ This function check obj is instace of a_class with isinstace function.

    Args:
        - obj (type: any): The obj to be chacked.
        - a_class (type: class): The class to check against.

    Returns:
        - (type: boolean): True if obj is intance of
        a_class while Flase if not.
    """
    return isinstance(obj, a_class)
