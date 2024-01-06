#!/usr/bin/python3
"""print squares."""


def print_square(size):
    """a function that prints a square with the character #."""
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square with the character #
    for i in range(size):
        print("#" * size)
