#!/usr/bin/python3
"""class Rectangle."""


class Rectangle:
    """defines a rectangle by: (based on 0-rectangle.py)."""

    def __init__(self, width=0, height=0):
        """Initializing rectangle.

        Args:
            height (int): height (int): The height of the rectangle.
            width (int): The width of the rectangle.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """setting The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
