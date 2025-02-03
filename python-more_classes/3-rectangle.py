#!/usr/bin/python3
"""
Module: 3-rectangle.py
Description: A module defining a Rectangle class with string representation.

This module extends the previous Rectangle implementation by adding
string representation methods to print the rectangle using '#' character.
"""
class Rectangle:
    """
    A class representing a rectangle with string representation capabilities.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class provides methods to create string representations of the rectangle.
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
        
    # [Previous methods]
    
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
