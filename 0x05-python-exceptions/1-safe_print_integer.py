#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if the value is an integer and has been printed correctly, False otherwise.
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return (False)
    else:
        return (True)

