# Take the input of the number for printing the table
number = int(input("Enter the number: "))
# Validate that number is positive or not
if number<0:
  print("Table is not defined for negative number")
  exit()

for num in range(11):
  print(f"{number}X{number}={num*number}")