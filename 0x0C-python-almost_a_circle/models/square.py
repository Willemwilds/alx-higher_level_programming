#!/usr/bin/python3
"""
This module defines the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class inherits from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, size, x, y, id)

    def __str__(self):
        """
        String representation of the class
        """
        return "[Square] {} {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Gets the with of the square
        """
        return self.__width

    @size.setter
    def size(self, value):
        """
        Sets the width of the square
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the instances
        of the square.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the attributes of the class in dictionary form.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
