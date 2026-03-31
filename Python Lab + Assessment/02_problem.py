str = "Hellow"
dictionary = {}
ind = 0
for i in str:
    count = 0
    for j in str:
        if i == j:
            count += 1
    dictionary[i] = count

print(dictionary)
