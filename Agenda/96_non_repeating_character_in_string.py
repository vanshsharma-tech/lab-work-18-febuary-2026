# Find first non-repeating character in string.
def first_non_repeating_character(s):
    char_count = {}

    # Count the frequency of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char

    return None  # Return None if there is no non-repeating character


# Example usage
input_string = "swiss"
result = first_non_repeating_character(input_string)
if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("There is no non-repeating character in the string.")
