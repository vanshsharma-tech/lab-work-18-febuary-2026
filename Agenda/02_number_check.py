# Take the user input
num = int(input("Enter the number:"))
# check for positive number
if num > 0:
    print(f"{num} is a positive number")
# check for negative number
elif num < 0:
    print(f"{num} is a negative number")
# If the number is not positive and negative then it should be zero
else:
    print(f"{num} is a zero number")
