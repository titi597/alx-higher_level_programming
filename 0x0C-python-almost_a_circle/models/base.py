#!/usr/bin/python3
"""Module containing the Base class."""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries

        Args:
            json_string (str): JSON string

        Returns:
            list: List of dictionaries
        """
        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with all attributes already set

        Args:
            dictionary (dict): Dictionary of attributes

        Returns:
            Base: Instance with attributes set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                divnew = cls(1, 1)
            else:
                divnew = cls(1)
            divnew.update(**dictionary)
            return divnew

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file

        Returns:
            list: List of instances
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**dictionary) for dictionary in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a CSV file

        Args:
            list_objs (list): List of instances

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file

        Returns:
            list: List of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
