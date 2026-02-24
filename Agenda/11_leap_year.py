year = int(input("Enter a year: "))
if year < 0 or year > 9999:
    print("Year cannot be negative or greater than 9999.")
    exit()
# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
