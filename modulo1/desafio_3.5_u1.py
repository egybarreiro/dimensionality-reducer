"""
Purpose: This module contains a simple script to multiply a specific list of 5 numbers by 2.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

# This other function multiplies a list of numbers by 2.
numbers_list = [1, 2, 3, 4, 5]
result_list =[n * 2 for n in numbers_list]
print(f"The result of multiplying {numbers_list} by 2 is {result_list}")