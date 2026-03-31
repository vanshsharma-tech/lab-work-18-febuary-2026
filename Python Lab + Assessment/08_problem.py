# Swap keys and values in a dictionary
d = {"a": 1, "b": 2, "c": 3}

swapped = {}

for key, value in d.items():
    swapped[value] = key

print(swapped)