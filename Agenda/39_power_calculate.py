# Calculate the power without using exponent operator
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
# Check if the exponent is negative
if exponent < 0:
    print("Negative exponent is not supported.")
    exit()
# Calculate the power using a for loop
power = 1
for i in range(exponent):
    power *= base
# Print the result
print(f"{base} raised to the power of {exponent} is: {power}.")