import numpy as np

# Input array
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Replace odd numbers
arr[arr % 2 != 0] = -1

print(arr)