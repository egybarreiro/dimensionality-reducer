"""Purpose: This module contains a simple script to build a calculator that divides two numbers.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""



# Welcomes the user
print("Welcome to the Division Calculator 1.0!")

# Enabling loop
keep_calculating = True

while keep_calculating:
    print("Start your calculations.")

# Requesting numbers to work with
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

# Handling possible errors/exceptions
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")   
    
    else: 
        print(f"The result of dividing {num1} by {num2} is: {result}.")

    finally:
        print("Division successfully completed!")
    
    # Asking user if wants to keep using program or not
    answer = input("Would you like to divide other numbers? ")
    
    answer = answer.lower().strip()

    if answer == "no":
        keep_calculating = False
        print("Hope you've had fun, see you on the next one!")
        print("*********************************************************************")
    elif answer == "yes":
        keep_calculating = True
    else:
        while answer == input("Would you like to divide other numbers? "):
            print("Invalid answer.".upper())
            print("Please type 'yes' to start a new division or 'no' to close program.".upper())

    




