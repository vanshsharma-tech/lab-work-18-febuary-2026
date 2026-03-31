import numpy as np

# Create array from 1 to 25 and reshape to 5×5
arr = np.arange(1, 26).reshape(5, 5)

print("5x5 Matrix:\n", arr)

# Extract middle 3×3 sub-matrix
sub_matrix = arr[1:4, 1:4]

print("Middle 3x3 Sub-matrix:\n", sub_matrix)
