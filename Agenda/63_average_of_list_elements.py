# File Name: 63_average_of_list_elements.py
# Problem 63
# Find average of list elements using function

# Function to calculate average
def find_average(numbers):

    # If list is empty, avoid division by zero
    if len(numbers) == 0:
        return 0

    total = 0  # Variable to store sum

    # Calculate sum manually
    for num in numbers:
        total += num

    # Average formula = sum / number of elements
    average = total / len(numbers)

    return average


# -------- Main Program --------

# Input list (Example: 10 20 30 40)
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Call function
result = find_average(numbers)

# Output result
print("Average of list elements:", result)