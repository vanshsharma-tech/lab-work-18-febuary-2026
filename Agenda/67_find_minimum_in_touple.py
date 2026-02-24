# Find maximum in a tuple
numbers = (3, 1, 4, 1, 5, 9)
# code here
min_number = numbers[0]
for number in numbers:
    if number < min_number:
        min_number = number
# print the minimum number
print(min_number)
