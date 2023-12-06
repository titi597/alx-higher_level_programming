#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    new_matrix = []

    # Iterate over each row in the matrix
    for row in matrix:
        # Create a new row to store squared values for the current row
        new_row = []
        
        # Iterate over each element in the row and append its square to new_row
        for element in row:
            new_row.append(element ** 2)
        
        # Append the new_row to the new_matrix
        new_matrix.append(new_row)

    return new_matrix
