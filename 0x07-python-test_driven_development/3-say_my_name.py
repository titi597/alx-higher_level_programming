#!/usr/bin/python3
"""Say my name."""
def say_my_name(first_name, last_name=""):
    """a function that prints My name is <first name> <last name>."""
    # Check if first_name and last_name are strings
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string")

    # Print the formatted message
    print("My name is {} {}".format(first_name, last_name))
