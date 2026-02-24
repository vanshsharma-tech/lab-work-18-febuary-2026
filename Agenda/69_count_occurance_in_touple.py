# count occurrance of a number in a touple
numbers = (1, 2, 3, 4, 5, 1, 2, 1)
# code here
count = 0
for number in numbers:
    if number == 1:
        count += 1
# print the count
print(count)