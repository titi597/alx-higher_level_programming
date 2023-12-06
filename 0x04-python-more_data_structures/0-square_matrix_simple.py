#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix by copying the input matrix
    new_matrix = [row[:] for row in matrix]

    # Calculate the square values using nested list comprehension
    for i in range(len(new_matrix)):
        new_matrix[i] = [x**2 for x in new_matrix[i]]

    return new_matrix
