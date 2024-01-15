#!/usr/bin/python3
"""Module containing the Base class."""


class Base:
    """
    Base class for managing id attribute in other classes.

    Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for Base class.

        Args:
            id (int): Optional integer id. If provided, assigns it to the id,
                      otherwise, increments __nb_objects and new value to id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
