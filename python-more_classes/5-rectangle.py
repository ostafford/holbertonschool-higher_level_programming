#!/usr/bin/python3
"""
Module: 5-rectangle.py
Description: A module defining a Rectangle class with instance deletion handling.

This module extends the previous Rectangle implementation by adding
a __del__ method to print a message when a rectangle instance is deleted.
"""
class Rectangle:
    """
    A class representing a rectangle with instance deletion handling.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class provides a deletion method that prints a message on instance deletion.
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
    
    def __del__(self):
        """
        Handle rectangle instance deletion.
        
        Prints a goodbye message when the rectangle is deleted.
        """
        print("Bye rectangle...")
