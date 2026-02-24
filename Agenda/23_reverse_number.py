# Reverse the of negative and positive number using while number 
number = int(input("Enter the number(number must be positive): "))
if number < 0:
    print("Negative numbers are not supported.")
    exit()
# Store the original number for later use
num = number
# Initialize the variable to store the reversed number
reversed_number = 0
# Reverse the number using a while loop
while number != 0:
    digit = number % 10  # Get the last digit
    reversed_number = (reversed_number * 10) + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number
# Print the result
print(f"The reverse of {num} is {reversed_number}.")