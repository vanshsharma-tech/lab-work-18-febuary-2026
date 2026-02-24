# check a cgaracter is in digit or alphabet
character = input("Enter a character: ")
# Validating the input to ensure it is a single character
if len(character) != 1:
    print("Please enter a single character.")
    exit()
# Check if the character is a digit 
if character.isdigit():
    print(f"{character} is a digit.")
# check if the character is an alphabet 
elif character.isalpha():
    print(f"{character} is an alphabet.")
# If the character is neither a digit nor an alphabet, print a message
else:
    print(f"{character} is neither a digit nor an alphabet.")
