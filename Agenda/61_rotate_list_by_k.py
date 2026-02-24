# File Name: 61_rotate_list_by_k.py
# Problem 61
# Rotate a list by K positions


# Function to rotate list by k positions
def rotate_list(numbers, k):

    n = len(numbers)

    # If list is empty
    if n == 0:
        return numbers

    # Handle cases where k > n
    k = k % n

    # Rotate list using slicing
    # Right rotation:
    # Last k elements + remaining elements
    rotated = numbers[-k:] + numbers[:-k]

    return rotated


# -------- Main Program --------

# Input list (example: 1 2 3 4 5)
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Input K value
k = int(input("Enter value of K: "))

# Call function
result = rotate_list(numbers, k)

# Output result
print("Rotated List:", result)
