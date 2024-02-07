#!/usr/bin/python3

"""
This module provides MyList class inheited from list class.
"""


class MyList(list):
    """
    MyClass inherit from list class.

    Methods:
    - print_sorted(self: MyList) -> None: print sorted instance values.
    """

    def print_sorted(self):
        print(sorted(self))
