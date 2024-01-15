#!/usr/bin/python3
"""Module containing the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X-coordinate of the rectangle (default is 0)
            y (int): Y-coordinate of the rectangle (default is 0)
            id (int): Optional integer id (default is None)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, attr_name, value):
        """Validate if the given value is an integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))

    def validate_positive(self, attr_name, value):
        """Validate if the given value is greater than 0"""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))

    def validate_non_negative(self, attr_name, value):
        """Validate if the given value is greater than or equal to 0"""
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))
