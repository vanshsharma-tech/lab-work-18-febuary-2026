import numpy as np

# Create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5, 5))

print("Matrix:\n", matrix)

# Find minimum and maximum
min_val = np.min(matrix)
max_val = np.max(matrix)

print("Minimum value:", min_val)
print("Maximum value:", max_val)