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
        
    # [Previous methods]
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
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
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
    
    def __del__(self):
        """
        Handle rectangle instance deletion.
        
        Decrements the number of instances and prints a goodbye message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
