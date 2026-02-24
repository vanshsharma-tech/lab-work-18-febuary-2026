# Reverse a number using a while loop
number = int(input("Enter a number to reverse: "))
original_number = number
reverse_number = 0
# Calculate the reverse of the number using a while loop
while number > 0:
    reverse_number = reverse_number * 10 + number % 10
    number //= 10
# Print the reverse of the number
print(f"The reverse of {original_number} is {reverse_number}")