# Sort dictionary by values
my_dict = {'a': 3, 'b': 1, 'c': 2}
# code here
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# print the sorted dictionary
print(sorted_dict)
