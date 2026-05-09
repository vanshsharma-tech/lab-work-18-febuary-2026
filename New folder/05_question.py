import numpy as np

# Create array from 1 to 25 and reshape to 5x5
matrix = np.arange(1, 26).reshape(5, 5)

# Extract middle 3x3 sub-matrix
# Rows: index 1 to 3, Columns: index 1 to 3
sub_matrix = matrix[1:4, 1:4]

# Print result
print(sub_matrix)

# Output:
# [[ 7  8  9]
#  [12 13 14]
#  [17 18 19]]