#!/usr/bin/python3
"""defining class rectangle."""


class Rectangle:
    """defines a rectangle by: (based on 5-rectangle.py).
    
    Attributes:
            number_of_instances (int): the number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectanlge.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """setting the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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

    def area(self):
        """returning area."""
        return self.__width * self.__height

    def perimeter(self):
        """returning the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        ret = []
        for i in range(self.__height):
            [ret.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                ret.append("\n")
        return ("".join(ret))

    def __repr__(self):
        ret = "Rectangle(" + str(self.__width)
        ret += ", " + str(self.__height) + ")"
        return (ret)

    def __del__(self):
        """printing message for deletion of rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
