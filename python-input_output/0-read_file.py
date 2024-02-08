#!/usr/bin/python3

"""
This module provides read_file function
"""


def read_file(filename=""):
    """ This function read the file contents and print it

    Args:
        filename (str, optional): The filename
        to be read and printed. Defaults to "".
    """
    with open(filename, encoding="utf-8") as file:
        contest = file.read()
        print(contest)
