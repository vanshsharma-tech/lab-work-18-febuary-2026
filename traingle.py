first_angle = int(input("Enter the first angle:"))
second_angle = int(input("Enter the second angle:"))
third_angle = int(input("Enter the third angle:"))

traingle = first_angle + second_angle + third_angle
if (first_angle>0 and second_angle>0 and third_angle>0) and (traingle == 180):
    print("It is in traingle form")
else:
    print("It is not in traingle form")