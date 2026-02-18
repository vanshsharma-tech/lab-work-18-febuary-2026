first_angle = int(input("Enter the first angle:"))
if first_angle<=0:
    print("Angle can't be a negative or zero value")
    exit(0)
else:
    second_angle = int(input("Enter the second angle:"))
    if second_angle<=0:
        print("Angle can't be a negative or zero value")
        exit(0)
    else:
        third_angle = int(input("Enter the third angle:"))
        if third_angle<=0:
            print("Angle can't be a negative or zero value")
            exit(0)
        else:
            traingle = first_angle + second_angle + third_angle
            if (first_angle>0 and second_angle>0 and third_angle>0) and (traingle == 180):
                print("It is in traingle form")
            else:
                print("It is not in traingle form")

