import numpy as np

# Create a 4×4 matrix
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print("Matrix:\n", matrix)

# Row-wise sum
row_sum = np.sum(matrix, axis=1)

# Column-wise sum
col_sum = np.sum(matrix, axis=0)

print("Row-wise sum:", row_sum)
print("Column-wise sum:", col_sum)
