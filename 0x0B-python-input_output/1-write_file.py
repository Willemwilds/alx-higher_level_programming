#!/usr/bin/python3
"""
This module defines a function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Returns the number of character written into the file
    """

    with open(filename, 'w') as file:
        return file.write(text)
