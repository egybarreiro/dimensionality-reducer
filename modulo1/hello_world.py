"""
Purpose: This module contains a simple function to print "Hello, world." into the console.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-15 Modified: 2026-07-15
"""
print("Hello, world.!")
print("Yo, this is my first Python module!")
print("**************")
print("Hello, Lariza!", "Hello, Christian!", "Hello, Jordan!", "Hello, everyone!")
print("**************")

# This variable stores the position in line.
line_position: int = 0
print("Line position:", line_position)

# This variable stores the last called client.
last_client: int = None
print("Last client:", last_client)

last_client = line_position
print("Last client:", last_client)

# Add client to the line and update the line position.

line_position += 1
print("Line position:", line_position)

#Creación de Variables
#Asignación de enteros
age: int = 30

#Una cadena
name: str = "John"

#Un flotante
temperature: float = 25.5

#Un booleano
is_student: bool = True

#Imprimiendo las variables
print("Age:", age)
print("Name:", name)
print("Temperature:", temperature)
print("Is student:", is_student)

#Operaciones con numeros
num1 = 10
num2 = 3

#Suma
sum: int = num1 + num2
#Resta
difference: int = num1 - num2
#Multiplicación
product: int = num1 * num2
#División
quotient: float = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

#Manipulación de cadenas
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print("Full name:", full_name)

#Concatenación de cadenas
greeting = "Hello, " + full_name + "!"
print(greeting)

#Convirtiendo un entero a una cadena
age_str = str(age)
print("Age as string:", age_str)

message = "I am " + age_str + " years old."
print(message)  

#Convirtiendo una cadena a un entero
number = 30
num = int(number)
print("Number as integer:", num + 10)
