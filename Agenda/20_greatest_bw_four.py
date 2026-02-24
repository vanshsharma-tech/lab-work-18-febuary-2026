# Find the greatest number between four numbers
# Get user input for four numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
# Find the greatest number
greatest = num1  # Assume num1 is the greatest initially
if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3
if num4 > greatest:
    greatest = num4
# Print the greatest number
print(f"The greatest number among {num1}, {num2}, {num3}, and {num4} is: {greatest}")
