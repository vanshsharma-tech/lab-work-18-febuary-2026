import numpy as np

numbers_array = np.arange(1, 11)
numbers_array[numbers_array % 2 == 0] = 0

print(numbers_array)

# Output:
# [1 0 3 0 5 0 7 0 9 0]