import numpy as np

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

# Normalize array between 0 and 1
# Formula: (x - min) / (max - min)
normalized = (arr - arr.min()) / (arr.max() - arr.min())

# Print results
print("Original Array:", arr)
print("Normalized Array:", normalized)

# Output:
# Original: [0.54 0.21 0.87 0.12 0.63]
# Normalized: [0.56 0.12 0.95 0.00 0.67]