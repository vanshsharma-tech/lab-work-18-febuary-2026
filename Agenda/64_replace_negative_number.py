# take the list of numbers and replace all negative numbers with 0
numbers = [-1, 2, -3, 4, -5]
# code here
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
# print the modified list
print(numbers)