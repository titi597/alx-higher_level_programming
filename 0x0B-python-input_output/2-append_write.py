#!/usr/bin/python3
"""Append to a file."""


def append_write(filename="", text=""):
    """a function that appends a string.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
