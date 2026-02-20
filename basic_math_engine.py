first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the second number:"))


def add_two_number(num1, num2):
    return num1 + num2


def sub_two_number(num1, num2):
    return num1 - num2


def product_two_number(num1, num2):
    return num1 * num2


def division_two_number(num1, num2):
    return num1 / num2


print(
    f"The addition of {first_number} and {second_number} is {add_two_number(first_number,second_number)}"
)
print(
    f"The subtraction of {first_number} and {second_number} is {sub_two_number(first_number,second_number)}"
)
print(
    f"The product of {first_number} and {second_number} is {product_two_number(first_number,second_number)}"
)
print(
    f"The division of {first_number} and {second_number} is {(division_two_number(first_number,second_number))}"
)
