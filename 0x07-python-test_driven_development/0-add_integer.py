#!/usr/bin/python3
"""a function that adds 2 integers."""
def add_integer(a, b=98):
    """
    Returns the addition of two integers.

    Parameters:
    - a (int): The first integer.
    - b (int, optional): The second integer. Default is 98.

    Returns:
    int: The sum of a and b.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
