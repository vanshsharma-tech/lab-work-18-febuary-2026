# Reverse a string using for loop
string = input("Enter the string: ")
# Check if the string is empty
if not string:
    print("The string is empty. Please enter a valid string.")
    exit()
reversed_str = ""
# Evaluate the reverse of the string
for ch in string:
    reversed_str = ch + reversed_str
print(f"The reversed string of {string} is {reversed_str}")
