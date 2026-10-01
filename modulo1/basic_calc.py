"""Purpose: This module contains a simple script to build a calculator that performs basic math operations like sum, subtract, divide and multiply.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

# Welcomes the user
print("**************************************")
print("Welcome to the Basic Calculator 1.0!")
print("**************************************")
print("Type 'exit' at anytime to close the calculator.")
print("")

# Enabling loop so program starts again
keep_calculating = True

while keep_calculating:
    print("Start your calculations.")


    # Requesting first number and validating input
    while True:
        value_a = input("Enter your first number: ")

        if value_a.lower() == "exit":
            keep_calculating = False
            break

        try:
            value_a = float(value_a)
            break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
    if keep_calculating == False:
        break

    # Requesting operator and validating input
    while True:
        operator = input("Enter the operator(+, -, *, /): ")
        if operator.lower() == "exit":
            keep_calculating = False
            break

        if operator in ["+", "-", "*", "/"]:
            break
        print("Invalid operator. Please use +, -, *, or /.")
    if keep_calculating == False:
        break


    # Requesting second number and validating input
    while True:
        value_b = input("Enter your second number.")

        if value_b.lower() == "exit":
            keep_calculating = False
            break

        try:
            value_b = float(value_b)
            if operator == "/" and value_b == 0:
                print("Division by zero is not allowed. Use a non-zero number.")

            else:
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    if keep_calculating == False:
        break


    # Executing mathematical operation
    result = None

    if operator == "+":
        result = value_a + value_b
    elif operator == "-":
        result = value_a - value_b
    elif operator == "*":
        result = value_a * value_b
    elif operator == "/":
        result = value_a / value_b

    # Showing result
    print("The result is:", result)
    print("Type 'exit' anytime to close calculator.")
    print("")


# Program's Farewell
print("****************************")
print("Thanks for using the Basic Calculator 1.0")
print("See you next time!")
print("****************************")
    


