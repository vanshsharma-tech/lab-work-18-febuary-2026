# Count uppercase and lowercase letters.
def count_uppercase_lowercase(s):
    uppercase_count = 0
    lowercase_count = 0

    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count


# Example usage
input_string = "Hello World!"
uppercase, lowercase = count_uppercase_lowercase(input_string)
print(f"Number of uppercase letters: {uppercase}")
