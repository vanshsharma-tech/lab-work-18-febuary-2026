# Find all pairs in a list whose sum equals a target value
arr = [1, 2, 3, 4, 5]
target = 5
size = len(arr)

pairs = []

for i in range(size):
    for j in range(i + 1, size):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))  # store as tuple

print(pairs)