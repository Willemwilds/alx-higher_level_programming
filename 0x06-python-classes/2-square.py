#!/usr/bin/python3

"""
    This module creates a Square class
"""


class Square:
    """
        This class initializes the size attribute
    """

    def __init__(self, size=0):
        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
