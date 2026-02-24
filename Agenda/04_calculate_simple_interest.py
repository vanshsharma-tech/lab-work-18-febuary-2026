principle = float(input("Enter the principle amount:"))
if principle < 0:
    print("Principle amount cannot be negative.")
    exit()
rate = float(input("Enter the rate of interest:"))
if rate < 0:
    print("Rate of interest cannot be negative.")
    exit()
time = int(input("Enter the time in years:"))
if time < 0:
    print("Time cannot be negative.")
    exit()
simple_interest = (principle * rate * time) / 100
print(f"The simple interest is {simple_interest}")
