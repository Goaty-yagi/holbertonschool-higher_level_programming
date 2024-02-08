#!/usr/bin/python3

"""
This module provides save_to_json_file
"""
import json


def save_to_json_file(my_obj: object, filename: str):
    """ This function write my_obj to the file.

    Args:
        - my_obj(object): object to wite in the file
        - filename (str): The filename
        to be open and my_obj to be written in.
    Return:
        - int ->: Number of char written in the file.
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        json.dump(my_obj, file)
