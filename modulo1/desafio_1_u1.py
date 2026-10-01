"""
Purpose: This module contains a simple script to Greet and Segregate users by age.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

# Greeting the user
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Welcome to the Medicaid Program.")
user_age = int(input("Please enter your age: "))
if user_age >= 65:
    print("You are qualified for Medicaid.")
elif user_age >= 18 and user_age < 65:
    print("You are not qualified for Medicaid.")
else:
    print("You are too young to apply for Medicaid.")