# remove spaces from the beginning and end of the string
def remove_spaces(s):
    start = 0
    end = len(s) - 1

    # Remove leading spaces
    while start <= end and s[start].isspace():
        start += 1

    # Remove trailing spaces
    while end >= start and s[end].isspace():
        end -= 1

    # Return the trimmed string
    return s[start : end + 1]


# Example usage
input_string = "   Hello, World!   "
print(f"String after removing spaces: '{remove_spaces(input_string)}'")
