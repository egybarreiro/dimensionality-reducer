""" Este desafio consiste en escribir una funicon para aplanar 
una lista anidada usando comprension de listas."""


nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

flat_list = []

for sub_list in nested_list:
    for i in sub_list:
        flat_list.append(i)

print(flat_list)


# Formato list comprehension

nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

flat_list = [i for sub_list in nested_list for i in sub_list]
print ("List comprehension result:", flat_list)

# Formato funcion con list comprehension 

nested_list = [[1,2,3], [4,5], [6]]

#salida debe ser [1, 2, 3, 4, 5, 6]

def list_flattner(nested_list):
    flat_list = [i for sub_list in nested_list for i in sub_list]
    return flat_list

print ("Using a function with list comprehension result:", list_flattner(nested_list))