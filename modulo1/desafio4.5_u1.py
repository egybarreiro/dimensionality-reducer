"""
Purpose: This module contains a simple script to loop numbers playing the FizzBuzz game substituing multiples of 3 with "Fizz" and multiples of 5 with "Buzz" and for multiples of both with "FizzBuzz".
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

print("Welcome to FizzBuzz!")
print("Write a number and press Enter. Write 'q' to quit.\n")

while True:
    user_input = input("Write a number: ")

    if user_input.lower() == "q":
        print("Quitting the game...")
        break

    if not user_input.isdigit():
        print("Please write a valid number.")
        continue

    num = int(user_input)

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
