import numpy as np

# Input array
arr = np.array([10, 25, 5, 40, 30])
value = 20

# Get indices
indices = np.where(arr > value)

print(indices)