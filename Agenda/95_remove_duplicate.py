# Remove duplicate characters from string.
def remove_duplicates(s):
    seen = set()
    result = ""

    for char in s:
        if char not in seen:
            seen.add(char)
            result += char

    return result

# Example usage
input_string = "hello world"
print(f"String after removing duplicates: '{remove_duplicates(input_string)}'")
