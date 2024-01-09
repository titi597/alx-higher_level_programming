#!usr/bin/python3
"""Class to JSON."""


def class_to_json(obj):
    """a function that returns the dictionary description with data structr."""
    return obj.__dict__
