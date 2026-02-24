# Genrate the fibonacci series using for loop
n = int(input("Enter the number of terms in the Fibonacci series: "))
# Initialize the first two terms of the Fibonacci series
a, b = 0, 1
# Generate the Fibonacci series using a for loop
print("Fibonacci series:")
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b  # Update the values of a and b
# Print a newline after the series
print()
# output
# Enter the number of terms in the Fibonacci series: 10
# Fibonacci series:
# 0 1 1 2 3 5 8 13 21
