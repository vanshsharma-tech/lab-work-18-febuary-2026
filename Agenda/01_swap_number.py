# Taking the input of two number from the user
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
# Print the value before swapping the value
print("Before swapping the first number and second number is ", num1, num2)
# swapping the value of num1 and num2 without using the third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
# Print the value after swapping the value
print("After swapping the first number and second number is ", num1, num2)
