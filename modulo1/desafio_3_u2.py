"""Purpose: This module contains a simple script to practice and understan tuples.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

#Desafio3: Opeaciones con Conjuntos: Crea dos conjuntos de numeros, por ejemplo, {1,2,3} y {3,4,5}. Encuentra la union, interseccion y diferencia de estos conjuntos. Agrega y elimina elementos del primer conjunto.
my_own_set_a = {7,8,9}
print(my_own_set_a)
my_own_set_b = {9,10,11}
print(my_own_set_b)
set_union = my_own_set_a.union(my_own_set_b)
print(my_own_set_a.union(my_own_set_b))
set_intersection = my_own_set_a.intersection(my_own_set_b)
print(my_own_set_a.intersection(my_own_set_b))
set_difference = my_own_set_a.difference(my_own_set_b)
print(my_own_set_a.difference(my_own_set_b))
my_own_set_a.add(10)
print(my_own_set_a.add(10))
my_own_set_a.remove(10)
print(my_own_set_a)

