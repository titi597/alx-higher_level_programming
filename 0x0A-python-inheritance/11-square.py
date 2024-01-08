#!/usr/bin/python3
"""Square #2."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Instantiates a Square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
