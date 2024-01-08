#!/usr/bin/python3
"""a class MyList that inherits from list."""


class MyList(list):
    """Inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
