# Calculate the sum of first N natural numbers using for loop
number = int(input("Enter the number: "))
total_sum = 0
# Calculate the sum of first N natural numbers using a for loop
for i in range(1, number + 1):
    total_sum += i
# Print the result
print(f"The sum of the first {number} natural numbers is: {total_sum}.")