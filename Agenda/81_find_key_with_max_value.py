# find key with maximum value in a dictionary
my_dict = {'a': 3, 'b': 1, 'c': 2}
# code here
max_key = max(my_dict, key=my_dict.get)
# print the key with the maximum value
print(max_key)