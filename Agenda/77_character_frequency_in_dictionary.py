# Count character frequency using dictionary.
text = "hello world"
# code here
char_frequency = {}
for char in text:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
# print the character frequency
print(char_frequency)