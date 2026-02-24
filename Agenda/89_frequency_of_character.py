# Find frequency of each character in string
def frequency_of_characters(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency

# Example usage
input_string = "hello world"
print(f"Frequency of characters in the string: {frequency_of_characters(input_string)}")