# Problem Statement: Check whether tuple elements are unique.
# Given a tuple, check whether all the elements in the tuple are unique or not. If all the elements are unique, print "All elements are unique". Otherwise, print "There are duplicate elements".
my_tuple = (1, 2, 3, 4, 5)
# code here
if len(my_tuple) == len(set(my_tuple)):
    print("All elements are unique")
else:
    print("There are duplicate elements")
