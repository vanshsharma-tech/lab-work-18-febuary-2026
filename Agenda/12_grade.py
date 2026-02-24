# input the marks 
marks = int(input("Enter the marks: "))
# Validating the marks to ensure they are between 0 and 100
if marks < 0 or marks > 100:
    print("Marks cannot be negative or greater than 100.")
    exit()
# Determine the grade based on the marks using if-elif-else statements
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")