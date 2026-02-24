# Problem: Find Maximum of Three Numbers using Function


# Function to find maximum of three numbers
def find_max(num1, num2, num3):

    # Assume num1 is maximum initially
    maximum = num1

    # Compare with num2
    if num2 > maximum:
        maximum = num2

    # Compare with num3
    if num3 > maximum:
        maximum = num3

    return maximum


# -------- Main Program --------

# Taking input from user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Calling the function
result = find_max(a, b, c)

# Printing the result
print("Maximum number is:", result)
