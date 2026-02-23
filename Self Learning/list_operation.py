# Python List Operations - All in One File


# print("=== Python List Operations ===\n")
# 1️ Creating a List
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)
# 2️ Accessing Elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
# 3️ Adding Elements
numbers.append(60)
print("\nAfter append(60):", numbers)
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)
numbers.extend([70, 80])
print("After extend([70, 80]):", numbers)
# 4️ Removing Elements
numbers.remove(25)
print("\nAfter remove(25):", numbers)
popped_value = numbers.pop()
print("After pop():", numbers)
print("Popped value:", popped_value)
# 5️ Updating Elements
numbers[0] = 100
print("\nAfter updating first element:", numbers)
# 6️ Slicing
print("\nSliced List (1:4):", numbers[1:4])
# 7️ Looping Through List
print("\nLooping through list:")
for num in numbers:
    print(num)
# 8️ List Length
print("\nLength of list:", len(numbers))
# 9️ Sorting
numbers.sort()
print("\nAfter sort():", numbers)
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)
#  Reversing
numbers.reverse()
print("\nAfter reverse():", numbers)
# 1️1️ Checking Element
print("\nIs 40 in list?", 40 in numbers)
# 1️2️ List Comprehension
squares = [x * x for x in numbers]
print("\nSquares using list comprehension:", squares)
# 1️3️ Copying List
new_list = numbers.copy()
print("\nCopied List:", new_list)
# 1️4️ Clearing List
new_list.clear()
print("After clear():", new_list)
