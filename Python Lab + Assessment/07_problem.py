arr = [1, 2, 3, 2, 1, 5, 6, 7]

result = []

for i in arr:
    if i not in result:
        result.append(i)

print(result)