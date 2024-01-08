#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class):
    """Returns True if obj is instance of specified class; otherwise False."""
    return type(obj) is a_class
