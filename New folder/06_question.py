import numpy as np

# Create 4x4 matrix
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# Calculate row-wise sum (axis=1 → rows)
row_sum = matrix.sum(axis=1)

# Calculate column-wise sum (axis=0 → columns)
col_sum = matrix.sum(axis=0)

# Print results
print("Row Sum:", row_sum)
print("Column Sum:", col_sum)

# Output:
# Row Sum: [10 26 42 58]
# Column Sum: [28 32 36 40]