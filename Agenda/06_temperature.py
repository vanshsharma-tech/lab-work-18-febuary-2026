# Convert the temperature from Celsius to Fahrenheit
calcius = float(input("Enter the temperature in Celsius: "))
# Validating the temperature to ensure it is not below absolute zero
if calcius < -273.15:
    print("Temperature cannot be below absolute zero.")
    exit()
# Calculating the temperature in Fahrenheit using the formula F = (C * 9/5) + 32
fahrenheit = (calcius * 9 / 5) + 32
print(f"The temperature in Fahrenheit is {fahrenheit}")