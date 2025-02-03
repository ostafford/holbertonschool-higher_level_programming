#!/usr/bin/python3
"""
Module: 4-rectangle.py
Description: A module defining a Rectangle class with eval() support.

This module extends the previous Rectangle implementation by adding
a repr() method to allow recreation of the rectangle instance using eval().
"""
class Rectangle:
    """
    A class representing a rectangle with eval() recreation support.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class provides a repr() method for instance recreation.
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        
    def __str__(self):
        """
        Create a string representation of the rectangle.
        
        Returns:
            str: A string of the rectangle using '#' characters.
            Returns an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])
    
    def __repr__(self):
        """
        Create a string representation for recreating the rectangle.
        
        Returns:
            str: A string that can be used with eval() to recreate the rectangle.
        """
        return f"Rectangle({self.width}, {self.height})"
