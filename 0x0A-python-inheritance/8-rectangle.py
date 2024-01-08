#!/usr/bin/python3
"""Rectangle."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class representing base geometry."""

    def __init__(self, width, height):
        """Instantiates a Rectangle with width and height.

        Args:
            width(int): the width of rectangle.
            height (int): the height of rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
