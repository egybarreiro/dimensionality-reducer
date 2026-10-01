"""Purpose: This module contains a simple script to practice and understan tuples.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

#Desafio2: Tuplas y Repeticion- Crea una tupla con los numeros del 1 al 5. Concatenar esta tupla con otra tupla de tu eleccion. Crear una nueva tupla que repita la tupla original 2 veces.
my_own_tuple = (1,2,3,4,5)
print(my_own_tuple)
new_tuple = (6,7)
print (new_tuple)
print(my_own_tuple + new_tuple)
even_more_tuple = my_own_tuple + new_tuple + (8,9,10)
print(even_more_tuple)
repeat_the_tuple = my_own_tuple * 2
print(my_own_tuple * 2)