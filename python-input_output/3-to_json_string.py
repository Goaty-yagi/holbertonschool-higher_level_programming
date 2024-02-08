#!/usr/bin/python3
""" This module provides to_json_string function
"""

import json


def to_json_string(my_obj):
    """ This function serialize the my_obj, and return json formatted string.

    Args:
        my_obj (any): The obj to be serialized.

    Returns:
        str: json formatted string.
    """
    return json.dumps(my_obj)
