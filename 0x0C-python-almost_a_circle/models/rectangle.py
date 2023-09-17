#!/usr/bin/python3
"""
This module defines the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The method Initializes the class atttributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width attribute of the class
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width attribute of the class
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        self.__width = value

    @property
    def height(self):
        """
        Gets the height attribute of the class
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Sets the width attribute of the class
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be > 0".format(value))
        self.__height = value

    @property
    def x(self):
        """
        Gets the x value of the class
        """
        return self.x

    @x.setter
    def x(self, value):
        """
        Sets the x value of the class
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__x = value

    @property
    def y(self):
        """
        Gets the y value of the class
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y value of the class
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value < 0:
            raise ValueError("{} must be >= 0".format(value))
        self.__y = value

    def area(self):
        """
        The method defines the area of the class
        """
        return self.__width * self.__height

    def display(self):
        """
        Dispalys the value of the width with '#'
        """
        for x in range(self.__x):
            print()
        for x in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """
        String representation of the class
        """
        return "[Rectangle] {} {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        The method updates the attributes of the class instance
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Dictionary representation of the class instance attribute
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
