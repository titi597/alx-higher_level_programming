#!/usr/bin/python3
"""Module containing the Base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file

        Args:
            list_objs (list): List of instances

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))
