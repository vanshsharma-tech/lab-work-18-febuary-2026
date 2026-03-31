# Find the second largest element from a list without using built-in sort
list = []
n = int(input("Enter the range of the list :"))

for i in range(n):
    num = int(input("Enter the value :"))
    list.append(num)



# Step 1: Find largest
max = list[0]
for i in list:
    if max < i:
        max = i

# Step 2: Find second largest
second_max = float("-inf")

for i in list:
    if i != max and i > second_max:
        second_max = i

if second_max == float("-inf"):
    print("No second largest element")
else:
    print("Second Largest:", second_max)
