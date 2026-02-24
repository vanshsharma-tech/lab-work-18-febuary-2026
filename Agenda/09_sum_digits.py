# input a number and calculate the sum of its digits
digit = int(input("Enter the number:"))
sum_of_digits = 0
# Calculate the sum of the digits using a while loop
while digit > 0:
    sum_of_digits += digit % 10
    digit //= 10
# Print the sum of the digits
print(f"The sum of the digits is {sum_of_digits}")