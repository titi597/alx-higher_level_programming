#!/usr/bin/python3
"""Module containing the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class

        Args:
            size (int): Size of the square
            x (int): X-coordinate of the square (default is 0)
            y (int): Y-coordinate of the square (default is 0)
            id (int): Optional integer id (default is None)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Override the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
