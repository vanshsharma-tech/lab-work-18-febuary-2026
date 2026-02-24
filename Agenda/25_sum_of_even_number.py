# Find the sum of even numbers within a given range
# Get user input for the range
end = int(input("Enter the ending number: "))
start = 0
# Initialize a variable to store the sum of even numbers
even_sum = 0
# Calculate the sum of even numbers in the range
if end < 0:
    for i in range(end, 2):
        if i % 2 == 0:
            even_sum += i

else:
    for num in range(start, end + 1):
        if num % 2 == 0:  # Check if the number is even
            even_sum += num  # Add the even number to the sum


# Print the result
print(f"The sum of even numbers from 0 to {end} is: {even_sum}.")
