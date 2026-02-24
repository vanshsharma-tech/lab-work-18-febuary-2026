# Problem 40
# Print multiplication tables from 1 to 10

# We use two nested loops:
# Outer loop → for numbers 1 to 10 (table number)
# Inner loop → for multiplying numbers 1 to 10

for table in range(1, 11):   # Loop for tables from 1 to 10
    print(f"\nMultiplication Table of {table}:")
    
    for multiplier in range(1, 11):  # Loop for multiplying from 1 to 10
        result = table * multiplier   # Calculate multiplication
        print(f"{table} x {multiplier} = {result}")