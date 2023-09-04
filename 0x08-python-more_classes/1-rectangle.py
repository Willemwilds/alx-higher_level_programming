#!/usr/bin/python3

"""
    This module deals creates Rectangle class.
"""


class Rectangle:
    """ Initialises width and height of Rectangle"""

    def __init__(self, width=0, height=0):
        """ Initialises width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets width"""
        self.__width = width

    @width.setter
    def width(self, width):
        """ Sets width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Gets height"""
        self.__height = height

    @height.setter
    def height(self, height):
        """Sets height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = height
