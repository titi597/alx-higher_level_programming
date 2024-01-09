#!/usr/bin/python3
"""Search and update."""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

    except FileNotFoundError:
        pass  # Do nothing if the file is not found
