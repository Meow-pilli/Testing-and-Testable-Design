import numpy as np

# Define the size of the diagonal matrix
matrix_size = 5

# Create a diagonal matrix with all ones
diagonal_matrix = np.eye(matrix_size)

# Add a row of all zeros at the top
new_row = np.zeros((1, matrix_size))
matrix_with_zeros_row = np.vstack((new_row, diagonal_matrix))

# Define the function
def function(x):
    return x**2 + 1

# Generate values for the function
x_values = np.arange(matrix_size)  # Assuming x values from 0 to matrix_size-1
function_values = function(x_values)

function_column = function_values.reshape(-1, 1)

function_column_with_zeros = np.vstack((np.zeros((1, 1)), function_column))

# Concatenate the function column to the matrix
matrix_with_function_column = np.hstack((matrix_with_zeros_row, function_column_with_zeros))

print(matrix_with_function_column)
