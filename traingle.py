a = int(input("Enter the first angle:"))
b = int(input("Enter the second angle:"))
c = int(input("Enter the third angle:"))

angle = a + b + c

if (a>0 and b>0 and c>0) and (angle == 180):
    print("It is in traingle form")
else:
    print("It is not in traingle form")