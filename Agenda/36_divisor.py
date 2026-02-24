# Print all divisors of a number
number = int(input("Enter the number: "))
# Validate that the number is positive
if number < 0:
    print("Divisors are not defined for negative number")
    exit()
print(f"The divisors of {number} are:")
# Calculate and print the divisors using a for loop
for i in range(1, number + 1):
    if number % i == 0:
        print(i)
