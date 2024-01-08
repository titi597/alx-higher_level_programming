#!/usr/bin/python3
"""My integer."""


class MyInt(int):
    """Class representing a rebel MyInt."""

    def __eq__(self, other):
        """Overrides the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Overrides the != operator."""
        return super().__eq__(other)
