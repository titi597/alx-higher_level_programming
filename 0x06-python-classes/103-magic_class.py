#!/usr/bin/python3

"""Python class MagicClass"""


import math

class MagicClass:
    """fucntioning magic class"""

    def __init__(self, radius=0):
        """initializing
        Args:
        radius: length of side of the square.
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """displaying area"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """displayingperimeter"""

        return 2 * math.pi * self.__radius
