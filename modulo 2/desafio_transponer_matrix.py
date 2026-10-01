""" Este desafio consiste en crear una funcion para 
transponer una matriz bidimensional."""


matrix = [[1,2,], [3,4], [5,6]]

#La salida transpuesta debe ser [[1, 3, 5], [2, 4, 6]]

T = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])

    T.append(row)

print(T)

# Formato list comprehension

T = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(T)

# Formato de funcion con list comprehension

def transpose(matrix):
    T = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return(T)
