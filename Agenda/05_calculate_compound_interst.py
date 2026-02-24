# This program calculates the compound interest based on user input for principle, rate of interest, and time in years.
# Taking the input of principle amount
principle = float(input("Enter the principle amount: "))
# Validating the principle amount to ensure it is not negative
if principle < 0:
    print("Principle amount cannot be negative.")
    exit()
# Taking the input of rate 
rate = float(input("Enter the rate of interest: "))
# Validating the rate to ensure it is not negative
if rate < 0:
    print("Rate of interest cannot be negative.")
    exit()
# Taking the input of time
time = int(input("Enter the time in years: "))
# Validating the time to ensure that it is not negative
if time < 0:
    print("Time cannot be negative.")
    exit()
# Calculating the compound interest
compound_interest = principle * (1 + rate / 100) ** time - principle
print(f"The compound interest is {compound_interest}")