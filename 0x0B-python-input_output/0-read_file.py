#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """a function that reads a text file (UTF8)."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
