str = "Vansh"
str_len = len(str)
for char in str:
    if str.count(char) == 1:
        print("First non repeating character is ", char)
        break
