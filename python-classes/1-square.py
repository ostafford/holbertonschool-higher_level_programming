#!/usr/bin/python3
"""Module that defines a Square class with size attribute"""


class Square:
    """Class that defines a square with a private size attribute.

    This class implements a basic square with a size parameter
    that is stored as a private instance attribute.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square
        """
        self.__size = size
