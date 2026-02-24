# Reverse a string without using slicing.
text = "Hello, World!"
# code here
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
# print the reversed string
print(reversed_text)
