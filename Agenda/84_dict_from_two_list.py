# Create dictionary from two lists.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
# code here
my_dict = {keys[i]: values[i] for i in range(len(keys))}
# print the created dictionary
print(my_dict)