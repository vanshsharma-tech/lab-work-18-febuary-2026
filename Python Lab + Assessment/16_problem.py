import numpy as np

# Input array
arr = np.array([10, 20, 30, 40, 50])

# Normalize
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(normalized)