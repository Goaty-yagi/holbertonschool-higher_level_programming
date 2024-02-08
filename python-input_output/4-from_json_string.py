#!/usr/bin/python3

""" This module provides from_json_string function
"""

import json


def from_json_string(my_str: str) -> object:
    """ This function deserialize the my_str, and return python object.

    Args:
        - my_str (int): The string to be deserialized.

    Returns:
        - str: python object.
    """
    return json.loads(my_str)
