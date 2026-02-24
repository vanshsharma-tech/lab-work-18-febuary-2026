# Separate even and odd numbers from a list


# Function to separate even and odd numbers
def separate_even_odd(numbers):

    even_list = []  # List to store even numbers
    odd_list = []  # List to store odd numbers

    # Traverse through each number in the list
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)  # Add to even list
        else:
            odd_list.append(num)  # Add to odd list

    return even_list, odd_list


# -------- Main Program --------

# Taking list input from user
# Example input: 1 2 3 4 5
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calling the function
even_numbers, odd_numbers = separate_even_odd(numbers)

# Printing results
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
