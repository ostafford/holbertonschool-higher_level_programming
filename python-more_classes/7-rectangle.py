#!/usr/bin/python3
"""
Module: 6-rectangle.py
Description: A module defining a Rectangle class with instance counting.

This module extends the previous Rectangle implementation by adding
a class attribute to track the number of rectangle instances.
"""
class Rectangle:
    """
    A class representing a rectangle with instance counting capabilities.
    
    Class Attributes:
        number_of_instances (int): Total number of Rectangle instances.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class tracks the creation and deletion of rectangle instances.
    """
    number_of_instances = 0
    
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.
        
        Increments the number of instances when a new rectangle is created.
        
        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        
    def __str__(self):
        """
        Create a string representation of the rectangle.
        
        Returns:
            str: A string of the rectangle using '#' characters.
            Returns an empty string if width or height is 0.
        """
        Rectangle = []
        for _ in range(self.height):
            Rectangle.append('#' * self.width)
        return '\n'.join(Rectangle)
    
    def __del__(self):
        """
        Handle rectangle instance deletion.
        
        Decrements the number of instances and prints a goodbye message.
        """
        print("Bye rectangle...")
