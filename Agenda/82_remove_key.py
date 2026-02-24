# Safely remove a key from dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b' # Key we want to remove
# code here 
if key_to_remove in my_dict:
    del my_dict[key_to_remove]
# print the dictionary after removing the key
print(my_dict)