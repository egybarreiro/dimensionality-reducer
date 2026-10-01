"""
Purpose: This module contains a simple script to loop numbers from 1 to 30 playing the FizzBuzz game substituing multiples of 3 with "Fizz" and multiples of 5 with "Buzz".
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

#FizzBuzz game from 1 to 30

input ("Press Enter to start the FizzBuzz game from 1 to 30...")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)