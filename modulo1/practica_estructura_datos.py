"""Purpose: This module contains a simple script topractice with data structures.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

#Listas
my_list = [1,2,3,'Python', 5.0]

#Operaciones Basicas
#Salida 1
print(my_list[0])

#Agregar Nuevo Elemento 
my_list.append('nuevo elemento')

#Eliminar un Elemento
my_list.remove(2)

#Segmentacion
#Salida de elementos 1 al 4
print(my_list[1:4]) 


#Tuplas
my_tuple = (1, 'hola', 3.14)

#Operaciones Basicas
#Acceso a elementos
#Salida: hola
print(my_tuple[1])

#Concatenacion: Combina tuplas usando '+'
new_tuple = my_tuple + (5,6)

#Repeticion: Repite tuplas usando '*'
repeat_tuple = my_tuple * 2


#Conjuntos
#Creacion de conjuntos
my_set = {1,2,3,4,5}

#Agregando elementos al conjunto usando '.add()'
my_set.add(6)

#Eliminando elementos al conjunto usando '.discard()' o ''.remove()'
my_set.discard(3)

#Operaciones de conjunto
another_set = {4,5,6,7}
union_set = my_set.union(another_set)


#Diccionarios
my_dict = {'nombre': 'Alicia', 'edad': 25, 'ciudad': 'Nueva York'}

#Operaciones basicas
#Acceso a Elementos:
print(my_dict['nombre']) 

#Agregar/Actualizar Elementos: Asigna valores a las claves
my_dict['edad'] = 26
my_dict['pais'] = 'EE.UU'

#Eliminar Elementos: Usa '.pop()' o '.del()'
my_dict.pop('ciudad')






