# File Name: 62_sum_of_list_elements.py
# Problem 62
# Find sum of list elements using function

# Function to calculate sum of list elements
def find_sum(numbers):
    """
    This function takes a list of numbers
    and returns the sum of all elements.
    """

    total = 0  # Initialize sum variable

    # Traverse through each element in the list
    for num in numbers:
        total += num  # Add each number to total

    return total


# -------- Main Program --------

# Input list (Example: 1 2 3 4 5)
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Call function
result = find_sum(numbers)

# Output result
print("Sum of list elements:", result)