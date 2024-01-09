#!/usr/bin/python3
"""Search and update."""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    with open(filename) as ropt:
        for line in ropt:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
