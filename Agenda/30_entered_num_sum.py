# Create an empty list for store the value untill user entered the 0
numbers = []
while True:
    # Take the input untill user does not entered 0
    num = int(input("Enter the number:"))
    # If the number is not zero then it stored in the numbers list
    if num != 0:
        numbers.append(num)
    else:
        break
sum_of_digit = 0
# Evaluate the sum of digits
for i in numbers:
    sum_of_digit += i
print(f"The sum of number untill 0 is entered is {sum_of_digit}")
