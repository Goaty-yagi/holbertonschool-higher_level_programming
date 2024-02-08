#!/usr/bin/python3

"""
This module provides read_file function
"""


def read_file(filename: str = ""):
    """ This function read the file contents and print it

    Args:
        - filename (str, optional): The filename
        to be read and printed. Defaults to "".
    """
    with open(filename, mode='r', encoding="utf-8") as file:
        contest = file.read()
        print(contest, end="")
