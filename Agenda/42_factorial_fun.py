# Problem: Find Factorial using Function


# Function to calculate factorial
def factorial(num):

    # Factorial is not defined for negative numbers
    if num < 0:
        return None

    result = 1  # Initialize result to 1

    # Loop from 1 to num
    for i in range(1, num + 1):
        result *= i  # Multiply result with current number

    return result


# -------- Main Program --------

# Taking input from user
number = int(input("Enter a number: "))

# Calling the function
fact = factorial(number)

# Checking if number was negative
if fact is None:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial =", fact)
