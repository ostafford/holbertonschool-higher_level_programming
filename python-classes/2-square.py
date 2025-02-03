#!/usr/bin/python3
"""Module that defines a Square class with validated size attribute"""


class Square:
    """Class that defines a square with a private size attribute.

    This class implements a square with size validation,
    ensuring the size is an integer and non-negative.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
