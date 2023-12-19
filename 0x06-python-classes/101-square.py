#!/usr/bin/python3

"""Print Square instance."""


class Square:
    """a class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize.

        Args:
             size (int): the new square size.
             position (int, int): the new square position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """"returning the current square of area."""
        return (self.__size ** 2)

    def my_print(self):
        """"print out the current area of the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """defining the print function for a square."""
        result = ""
        for _ in range(self.__position[1]):
            result += "\n"
        if self.__size != 0:
            for _ in range(self.__size - 1):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
            result += " " * self.__position[0] + "#" * self.__size
        return (result)
