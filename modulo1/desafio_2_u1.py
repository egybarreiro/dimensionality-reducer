""""
Purpose: This module contains a simple script to create a countdown timer.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

from time import time


countdown_time = int(input("Enter the countdown time in seconds: "))
while countdown_time > 0:
    print(f"Time left: {countdown_time} seconds")
    countdown_time -= 1
print("Time is over!")
