#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file.
    """

    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file_2:
        file_2.write(text)
