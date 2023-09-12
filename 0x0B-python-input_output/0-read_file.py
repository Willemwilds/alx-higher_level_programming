#!/usr/bin/python3
"""
This module writes a function that reads a text file
"""


def read_file(filename=""):
    """
    This function prints the content of the file  into
    standard output.
    """

    with open(filename) as f:
        print(f.read(), end='')
