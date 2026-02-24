# Count the number of vowels in a string
input_string = input("Enter a string: ")
if not input_string:
    print("The string is empty. Please enter a valid string.")
    exit()
vowels = "aeiouAEIOU"
vowel_count = 0
# Count the vowels using a for loop
for char in input_string:
    if char in vowels:
        vowel_count += 1
# Print the result
print(f"The number of vowels in the string is: {vowel_count}.")