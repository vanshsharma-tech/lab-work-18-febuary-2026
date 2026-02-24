# Problem 43
# Check Palindrome String using Function


# Function to check whether a string is palindrome or not
def is_palindrome(text):

    # Convert string to lowercase to make comparison case-insensitive
    text = text.lower()

    # Reverse the string using slicing
    reversed_text = text[::-1]

    # Compare original string with reversed string
    if text == reversed_text:
        return True
    else:
        return False


# -------- Main Program --------

# Taking input from user
string_value = input("Enter a string: ")

# Calling the function
if is_palindrome(string_value):
    print("Palindrome String")
else:
    print("Not a Palindrome String")
