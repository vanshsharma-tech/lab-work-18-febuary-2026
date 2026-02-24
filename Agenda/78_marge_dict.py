# Merge two dictionaries manually.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# code here
merged_dict = dict1.copy()  # Start with a copy of the first dictionary
merged_dict.update(dict2)  # Update with the second dictionary
# print the merged dictionary
print(merged_dict)
