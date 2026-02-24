# Check the number of lies within the given range
# Get user input for the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
number = int(input("Enter the number: "))
# Check for lies in the range
if number >= start and number <= end:
    print("Number is lies in the given range")
else:
    print("Number does n't lies with in the given range")
