value = input("Enter the string: ")
count = 0
for i in value:
  if not i.isalnum():
    count += 1

print(count)