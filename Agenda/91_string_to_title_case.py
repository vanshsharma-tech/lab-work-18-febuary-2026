# string to title case manually without using built-in functions
def string_to_title_case(s):
    result = ""
    in_word = False

    for char in s:
        if char.isspace():
            result += char
            in_word = False
        else:
            if not in_word:
                result += char.upper()  # Capitalize the first letter of the word
                in_word = True
            else:
                result += char.lower()  # Convert the rest of the letters to lowercase

    return result


input_string = "hello world!."
print(f"String in title case: '{string_to_title_case(input_string)}'")
