# Count number of words in a string without using built-in functions
def count_words(s):
    count = 0
    in_word = False

    for char in s:
        if char.isspace():
            if in_word:
                count += 1
                in_word = False
        else:
            in_word = True

    # If the last character is not a space, count the last word
    if in_word:
        count += 1

    return count


# Example usage
input_string = "Hello, how are you doing today?"
print(f"Number of words in the string: {count_words(input_string)}")
