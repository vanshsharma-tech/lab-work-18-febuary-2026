# Flatten a nested list
arr = [1, [2, [3, 4], 5], 6]


def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))  # recursion
        else:
            result.append(i)
    return result


arr = [1, [2, [3, 4], 5], 6]
print(flatten(arr))
