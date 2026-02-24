# Python String Operations - All in One File


print("=== Python String Operations ===\n")
# 1️ Creating a String
text = "Hello World"
print("Original String:", text)
# 2️ Accessing Characters
print("First character:", text[0])
print("Last character:", text[-1])
# 3️ String Slicing
print("\nSlice (0:5):", text[0:5])
print("Slice (6:):", text[6:])
# 4️ String Length
print("\nLength of string:", len(text))
# 5️ Changing Case 
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
# 6️ Removing Spaces
spaced_text = "   Python Programming   "
print("\nBefore strip():", spaced_text)
print("After strip():", spaced_text.strip())
# 7️ Replacing Text world to python
new_text = text.replace("World", "Python")
print("\nAfter replace():", new_text)
# 8️ Splitting String
sentence = "Python is very powerful"
words = sentence.split()
print("\nAfter split():", words)
# 9️ Joining List into String
joined = "-".join(words)
print("After join():", joined)
# 10 Checking Substring
print("\nIs 'Hello' in text?", "Hello" in text)
# 1️1️ Finding Index
print("\nIndex of 'World':", text.find("World"))
# 1️2️ Count Occurrences
print("\nCount of 'l':", text.count("l"))
# 1️3️ Checking String Type it return the condition is true or not
num = "12345"
print("\nIs numeric?", num.isnumeric())
alpha = "Python"
print("Is alphabetic?", alpha.isalpha())
alnum = "Python123"
print("Is alphanumeric?", alnum.isalnum())
# 1️4️ String Formatting
name = "Vansh"
age = 21
formatted = f"My name is {name} and I am {age} years old."
print("\nFormatted String:", formatted)
