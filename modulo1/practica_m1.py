"""
Purpose: This module contains a simple function to print and modify several variables as practice and print them into the console.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-16 Modified: 2026-07-16
"""

# Different types of variables
from queue import Full


name = "Egy" #string (text)
age = 32 #int (integer o entero)
height = 1.78 #float (decimal)
student = True #bool (booleano)

print ("Name:", name)
print ("Age:", age)
print ("Height:", height)
print ("Student?", student)

# Changing the values of the variables
name = "Egy Barreiro"
age = 33
height = 1.79
student = False

print ("Name:", name)
print ("Age:", age)
print ("Height:", height)
print ("Student?", student)

# Changing the printed values of the variables
print ("--- After Modification ---")
print ("New Name:", name)
print ("New Age:", age)
print ("New Height:", height)
print ("New Student?", student)

# Creating additional variables to test my code capabilities
city = "Las Piedras"
birth_year = 1990
weight = 75.5
has_children = True
how_many_children = 1

print ("City:", city)
print ("Birth Year:", birth_year)
print ("Weight:", weight)
print ("Has Children?", has_children)
if has_children:
    print ("How many children:", how_many_children)

# Challenge of Basic Math Operations using variables
# Variables
x = 10
y = 5
z = 2
a = 3

# Operations
sum_result = x + y + z + a
difference_result = x - y - z - a
product_result = x * y * z * a
power_result = x ** z  # x raised to the power of z

print ("Sum:", sum_result)
print ("Difference:", difference_result)
print ("Product:", product_result)
print ("Power:", power_result)

# Challenge of String Manipulation using variables
#Variables
first_name = "Egy"
last_name = "Barreiro"
full_name = first_name + " " + last_name

print ("First Name:", first_name)
print ("Last Name:", last_name)
print ("Full Name:", full_name)

#Confirming understanding of string manipulation
#Variables
message = "Estoy aprendiendo Python." 
institution = "Terminal 34"
city = "Las Piedras"
Sentence = message + " " + institution + " " + city

print (Sentence)
print (Sentence.upper()) # Convert to uppercase
print (message.replace("aprendiendo Python.", "estudiando Python en")) # Replace a word in the string
print (message.replace("aprendiendo Python.", "estudiando Python en " + institution + " " + city)) # Replace a word in the string with additional information
print (Sentence.replace("Estoy aprendiendo Python.", "Estoy estudiando Python en " + institution + " " + city)) # Replace a word in the string with additional information
print (Sentence.replace("Estoy aprendiendo Python.", "Estoy estudiando Python en ").upper()) # Replace a word in the string with additional information and convert to uppercase

#Adding int to string to print a message with a variable
terminal_number = 34
text = "Me está gustando mucho el curso de Python en Terminal " + str(terminal_number) + "."
print (text)    

#Understanding Boolean logic with variables 
#Variables
is_raining = False
is_sunny = True
need_umbrella = is_raining and not is_sunny

print ("Need umbrella?", need_umbrella)
print ("Is it raining?", is_raining)
print ("Is it sunny?", is_sunny)
print ("Is it raining and sunny?", is_raining and is_sunny)
