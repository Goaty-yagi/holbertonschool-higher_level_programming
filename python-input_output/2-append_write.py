#!/usr/bin/python3

"""
This module provides append_write function
"""


def append_write(filename: str = "", text: str = "") -> int:
    """ This function append the text to the file
    at the last content.

    Args:
        - filename (str, optional): The filename
        to be read. Defaults to "".
        - text(str, optional): The text to be appended in
        the file. Defaults to "".
    Return:
        - int ->: Number of char written in the file.
    """
    with open(filename, mode='a+', encoding="utf-8") as file:
        count = file.write(text)
        return count
