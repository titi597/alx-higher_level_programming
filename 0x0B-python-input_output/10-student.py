#!/usr/bin/python3
"""Student to JSON with filter."""


class Student:
    """a class Student that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializing the student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            filtered_attributes = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_attributes[attr] = getattr(self, attr)
            return filtered_attributes
