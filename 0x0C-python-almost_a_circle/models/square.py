#!/usr/bin/python3
"""
This module creates the class Square which inherits from the Rectangle class
The module module deals with squares
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is the Square class which inherits from the
    Rectangle class. The class also defines the
    attributes of a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width  # Since size is equal to width and height

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value  # Set both width and height to the same value

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
