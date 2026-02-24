# Function to calculate the factorial of a number
def factorial(number):
    
    # Check if the number is 0
    # Factorial of 0 is always 1
    if number == 0:
        return 1

    # Check if the number is negative
    # Factorial is not defined for negative numbers
    if number < 0:
        return "Cannot find factorial of a negative number"

    fact = 1

    # Loop from 1 to the given number (inclusive)
    # Multiply each number to calculate factorial
    for i in range(1, number + 1, 1):
        fact *= i   # fact = fact * i

    # Return the formatted result
    return f"The factorial of {number} is {fact}"


# Function call factorial(5)
print(factorial(5))