#!/usr/bin/python3
"""
Module: 8-rectangle.py
Description: A module defining a Rectangle class with rectangle comparison capabilities.

This module extends the previous Rectangle implementation by adding
a static method to compare rectangles based on their area.
"""
class Rectangle:
    """
    A class representing a rectangle with comparison capabilities.
    
    Class Attributes:
        number_of_instances (int): Total number of Rectangle instances.
        print_symbol (any): Symbol used for string representation of the rectangle.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class provides a method to compare rectangles based on their area.
    """
    number_of_instances = 0
    print_symbol = "#"
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Increments the number of instances when a new rectangle is created.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
  
    def area(self):
        return self.width * self.height
        
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
    
    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        """
        Compare two rectangles and return the one with the larger area.
        
        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.
        
        Returns:
            Rectangle: The rectangle with the larger or equal area.
        
        Raises:
            TypeError: If either argument is not a Rectangle instance.
        """
        if not isinstance(rect_1, cls):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, cls):
            raise TypeError("rect_2 must be an instance of Rectangle")
    
    def __del__(self):
        """
        Handle rectangle instance deletion.
        
        Decrements the number of instances and prints a goodbye message.
        """
        print("Bye rectangle...")
