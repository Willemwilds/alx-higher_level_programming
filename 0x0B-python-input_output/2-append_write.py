#!/usr/bin/python3
""""
This module defines a function that appends a string to an
existing file.
"""


def append_write(filename="", text=""):
    """
    This function returns the number of characters added to
    the existing file.
    """

    with open(filename, 'a') as file:
        return file.write(text)
