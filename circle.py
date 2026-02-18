radius = float(input("Enter the redius of circle (in Cm.):"))
if radius < 0:
    print("Radius can't be negative")
    exit()
else:
    pi = 3.14
    print("The area of circle is ", (pi * radius**2))
    print("The Perimeter (Circumference) of the circle is ", 2 * pi * radius)
