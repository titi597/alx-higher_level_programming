#!/usr/bin/python3
"""Say my name."""


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first and last names.

    Parameters:
    - first_name (str): The first name.
    - last_name (str, optional): The last name. Default is an empty string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
