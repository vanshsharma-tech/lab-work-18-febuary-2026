value = int(input("Enter the number:"))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 13, 4, 56, 67, 4, 35, 4, 56, 7, 8]
ind = numbers.index(value)
# print(ind)
for i in range(len(numbers)-1,ind,-1):
  if numbers[i]==value:
    numbers.pop(i)
print(numbers)