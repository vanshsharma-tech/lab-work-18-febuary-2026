# check a character is vowel or consonant
character = input("Enter a character: ")
# Validating the input to ensure it is a single character
if len(character) != 1:
    print("Please enter a single character.")
    exit()
# Check if the character is an alphabet and determine if it is a vowel or consonant
if character.isalpha():
    if character.lower() in "aeiou":
        print(f"{character} is a vowel.")
    else:
        print(f"{character} is a consonant.")
