# Find common elements between two lists without using set
list1 = [1, 2, 3, 4]
list2 = [20, 2, 4, 6]
list3 = []
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)

print(list3)
