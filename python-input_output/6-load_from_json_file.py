#!/usr/bin/python3

"""
This module provides load_from_json_file.
"""
import json


def load_from_json_file(filename: str) -> object:
    """ This function opem the file and create python object.

    Args:
        - filename (str): The filename
        to be open and deserialized to python obj.
    Return:
        - object ->: python obj created.
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        python_obj = json.load(file)

        return python_obj
