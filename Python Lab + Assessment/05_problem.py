# Input list of tuples (name, marks)
students = [("Vansh", 85), ("Aman", 92), ("Riya", 78), ("Karan", 88)]

# Sort based on marks (2nd element)
sorted_list = sorted(students, key=lambda x: x[1])

print(sorted_list)