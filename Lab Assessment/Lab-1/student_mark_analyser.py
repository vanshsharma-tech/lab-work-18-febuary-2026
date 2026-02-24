n = int(input("How many student? "))
if n < 0:
    print("Student number must be in positive value")
    exit()
lst = []

for i in range(n):
    value = int(input())
    lst.append(value)
for i in lst:
    if i < 0 or i > 100:
        lst.remove(i)

total_marks = 0

max_mark = lst[0]
for mark in lst:
    total_marks += mark
    if max_mark < mark:
        max_mark = mark

average_marks = total_marks / len(lst)

print(f"The average marks is {average_marks}")
print(f"Highest mark is {max_mark}")

if average_marks > 90 and average_marks <= 100:
    print("A")
elif average_marks > 80 and average_marks <= 90:
    print("B")
elif average_marks > 70 and average_marks <= 80:
    print("C")
elif average_marks > 50 and average_marks <= 70:
    print("D")
elif average_marks > 35 and average_marks <= 50:
    print("D")
else:
    print("F")
