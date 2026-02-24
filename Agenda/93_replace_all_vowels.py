# Replace all vowels in a string with *
word = "Hello, World!"


def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char in vowels:
            result += "*"
        else:
            result += char

    return result


print(f"String after replacing vowels: '{replace_vowels(word)}'")
