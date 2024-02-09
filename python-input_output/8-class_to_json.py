#!/usr/bin/python3

""" This module provides class_to_json function.
"""


def class_to_json(obj):
    """ This function retrieve dict from the object, and return it.

    Args:
        - obj (object): The obj that dict will be retrieved from.

    Returns:
        - dicr: The dict from the obj
    """
    obj_dict = obj.__dict__
    return obj_dict
