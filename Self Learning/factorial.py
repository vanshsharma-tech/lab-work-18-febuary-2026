def factorial(number):
    if number == 0:
        return 1
    if number < 0:
        return "Can't possible to find the factorial of negative number"
    fact = 1
    for i in range(1, number + 1):
        fact *= i

    print(f"The factorial of {number} is {fact}")
