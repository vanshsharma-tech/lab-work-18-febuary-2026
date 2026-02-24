number = int(input("Enter the number: "))
num = number
if number<0:
  print("Factorial is not defined for negative numbers.")
elif number == 0 or number == 1:
  print(f"The factorial of {number} is 1.")
else:
  factorial = 1
  while(number > 1):
    factorial *= number
    number -= 1
  print(f"The factorial of {num} is {factorial}.")