""" Este desafio consiste en escribir una funcionque tome un 
arreglo bidimensional y devuelva la suma de cada fila como uan lista."""


matrix = [[1,2,3], [4,5,6]]

#salida debe ser [6, 15]

def sum_rows(matrix):
    return [sum(row) for row in matrix]

print(sum_rows(matrix))






