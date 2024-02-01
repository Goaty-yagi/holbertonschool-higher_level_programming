#!/usr/bin/python3

"""
Provides a function for printing a person's name.

Function:
    - say_my_name(first_name, last_name=""): Prints the
    provided first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the provided first and last name.

    Parameters:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed.
        Defaults to an empty string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
