#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []  # Initialize an empty list to hold the new matrix
    for row in matrix:  # Iterate over each row in the input matrix
        new_row = []  # Initialize an empty list for the current new row
        for x in row:  # Iterate over each element in the current row
            new_element = x ** 2  # Compute the square of the element
            new_row.append(new_element)  # Append the squared value to the new row
        new_matrix.append(new_row)  # Add the new row to the new matrix
    return new_matrix  # Return the newly created matrix with squared values
