num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))

if num1 > num2 and num1 > num3:
    print(f"First number {num1} is largest")
elif num2 > num1 and num2 > num3:
    print(f"Second number {num2} is largest")
elif num3 > num1 and num3 > num2:
    print(f"Third number {num3} is largest")
else:
    print("All numbers are equal")
