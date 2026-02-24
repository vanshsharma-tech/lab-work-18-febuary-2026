# Find maximum in a tuple
numbers = (3, 1, 4, 1, 5, 9)
# code here
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
# print the maximum number
print(max_number)
