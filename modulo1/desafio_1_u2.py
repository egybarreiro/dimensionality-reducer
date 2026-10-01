"""Purpose: This module contains a simple script to practice and understand lists.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

#Desafio1: Manipulacion de Listas- Crea una lista de tus 5 frutas favoritas. Agrega otra fruta a la lista. Elimina la segunda fruta de la lista. Imprime l aultima fruta de la lista.
my_fruits_list = ['bananna', 'apple', 'grape', 'pineapple', 'pear']
print(my_fruits_list)
my_fruits_list.append('strawberry')
print(my_fruits_list)
my_fruits_list.remove(my_fruits_list[1])
print(my_fruits_list)
print(my_fruits_list[-1])