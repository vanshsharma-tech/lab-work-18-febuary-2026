# Check whether string contains only digits
def contains_only_digits(s):
    return s.isdigit()
# Example usage
input_string = "12345"
if contains_only_digits(input_string):
    print(f"The string '{input_string}' contains only digits.")
else:
    print(f"The string '{input_string}' does not contain only digits.")