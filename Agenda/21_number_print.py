# Take the range to printing the number
end = int(input("Enter the ending number: "))
# initialize the starting number
num = 1
while num <= end:
    # print the number 
    print(num, end="")
    if num != end:
        print(end=", ")
    num += 1
