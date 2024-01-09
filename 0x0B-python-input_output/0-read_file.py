#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """a function that reads a text file (UTF8)."""

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content, end="")
    except FileNotFoundError:
        pass  # Do nothing if the file is not found
