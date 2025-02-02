#!/usr/bin/python3
"""
This module provides matrix division functionality.
It contains a single function that divides all elements of a matrix.
The function ensures proper validation of inputs and handles
division of integers and floats within the matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements in a matrix by a given number.
    Each element in the matrix is divided by div and rounded to 2 decimal places.
    The input matrix must be a list of lists containing only integers or floats.
    All rows in the matrix must be of equal length.

    Args:
        matrix (list): A list of lists containing integers or floats
        div (int or float): The number to divide all elements by

    Returns:
        list: A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  if rows are of different sizes,
                  or if div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) 
              for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
