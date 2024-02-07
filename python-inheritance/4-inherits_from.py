#!/usr/bin/python3

"""
This module provides inherits_from function.
"""


def inherits_from(obj, a_class):
    """ This function check obj is instace of a subclass inherits from a_class.

    Args:
        - obj (type: any): The obj to be chacked.
        - a_class (type: class): The class to check against.

    Returns:
        - (type: boolean): True if obj is intance of
        a subclass inherits from a_class while Flase if not.
    """
    return issubclass(obj.__class__, a_class) and not obj.__class__ == a_class
