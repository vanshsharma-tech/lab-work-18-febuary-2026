# Problem: Check Prime Number using Function


# Function to check whether a number is prime or not
def is_prime(num):

    # Prime numbers are greater than 1
    if num <= 1:
        return False

    # Check divisibility from 2 to square root of number
    # We use sqrt optimization to reduce time complexity
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible, not prime

    return True  # If no divisors found, it is prime


# -------- Main Program --------

# Taking input from user
number = int(input("Enter a number: "))

# Calling the function
if is_prime(number):
    print("Prime Number")
else:
    print("Not a Prime Number")
