lst = [1,2,3,2,1]
# check if the list is a palindrome
is_palindrome = True
for i in range(len(lst) // 2):
    if lst[i] != lst[len(lst) - 1 - i]:
        is_palindrome = False
        break
print(is_palindrome)
