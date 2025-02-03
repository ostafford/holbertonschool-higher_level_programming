#!/usr/bin/python3
"""
Module: 1-rectangle.py
Description: A module defining a Rectangle class
with width and height attributes.
This module provides a Rectangle class
with private width and height attributes,
implementing getter and setter methods
with type and value validation.
"""


class Rectangle:
    """
    A class representing a rectangle
    with width and height.
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    The class validates width and height
    to ensure they are non-negative integers.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for the width of the rectangle.
        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle.
        Args:
            value (int): The width to set.
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle.
        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle.
        Args:
            value (int): The height to set.
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
