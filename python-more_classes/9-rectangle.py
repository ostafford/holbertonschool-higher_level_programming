#!/usr/bin/python3
"""
Module: 9-rectangle.py
Description: A comprehensive Rectangle class with advanced features.

This module provides a fully-featured Rectangle class with:
- Width and height validation
- Area and perimeter calculation
- Instance and class tracking
- Comparison methods
- String representation
- Square creation
"""
class Rectangle:
    """
    A comprehensive class representing a rectangle with multiple features.
    
    Class Attributes:
        number_of_instances (int): Total number of Rectangle instances.
        print_symbol (any): Symbol used for string representation of the rectangle.
    
    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    
    The class supports various operations including:
    - Width and height validation
    - Area and perimeter calculation
    - Instance counting
    - Custom string representation
    - Rectangle comparison
    - Square creation
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
        
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            int: The perimeter of the rectangle.
            Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """
        Create a string representation of the rectangle.
        
        Returns:
            str: A string of the rectangle using print_symbol.
            Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])
    
    def __repr__(self):
        """
        Create a string representation for recreating the rectangle.
        
        Returns:
            str: A string that can be used with eval() to recreate the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"
    
    def __del__(self):
        """
        Handle rectangle instance deletion.
        
        Decrements the number of instances and prints a goodbye message.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
        
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
    
    @classmethod
    def square(cls, size=0):
        """
        Create a square Rectangle instance.
        
        Args:
            size (int, optional): The size of the square. Defaults to 0.
        
        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)
