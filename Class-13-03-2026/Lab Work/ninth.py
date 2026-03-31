import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

print("Original Array:")
print(arr)

# Normalize the array between 0 and 1
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("\nNormalized Array:")
print(normalized)