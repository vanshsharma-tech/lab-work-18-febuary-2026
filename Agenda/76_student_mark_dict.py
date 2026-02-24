# Create student marks dictionary and find topper.
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}
# code here
topper = max(student_marks, key=student_marks.get)
# print the name of the topper
print(topper)