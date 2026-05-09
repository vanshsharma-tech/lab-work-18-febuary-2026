import numpy as np

# Create array from 1 to 15
arr = np.arange(1, 16)

# Find elements greater than 10
# Condition: arr > 10
result = arr[arr > 10]

# Print result
print(result)

# Output:
# [11 12 13 14 15]