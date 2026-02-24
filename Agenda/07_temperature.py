# input the temperature in Fahrenheit
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
# Validating the temperature to ensure it is not below absolute zero
if fahrenheit < -459.67:
    print("Temperature cannot be below absolute zero.")
    exit()
# Calculating the temperature in Celsius using the formula C = (F - 32) * 5/9
calcius = (fahrenheit - 32) * 5 / 9
print(f"The temperature in Celsius is {calcius}")
