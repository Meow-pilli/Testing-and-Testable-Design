import numpy as np

def create_diagonal_matrix(n):
    matrix = np.eye(n)  # Create an identity matrix of size n x n
    return matrix

def add_row(matrix):
    row_of_zeros = np.zeros((1, matrix.shape[1]))  # Create a row of zeros
    matrix = np.vstack((row_of_zeros, matrix))  # Add the row of zeros on top
    return matrix

def add_column(matrix, func):
    x_values = np.arange(0, matrix.shape[0])  # Generate x values from 1 to n
    column_values = func(x_values)  # Calculate column values using the given function
    column_values = column_values.reshape((matrix.shape[0], 1))  # Reshape to column vector
    matrix = np.hstack((matrix, column_values))  # Add the column to the matrix
    return matrix

def function(x):
    y=((x**2) + 1)
    return np.where(y % 2 == 0, 0, 1)  # Function x^2 + 1 for odd values of y, 0 for even values

n = 5  # Size of the square matrix
diagonal_matrix = create_diagonal_matrix(n)
diagonal_matrix_with_zeros_row = add_row(diagonal_matrix)
final_matrix = add_column(diagonal_matrix_with_zeros_row, function)

print(final_matrix)
