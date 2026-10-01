#Desafio 1: Comprension de Lista con Filtrado --> Crea una lista de numeros pares entre 1 y 20 usando una comprension de listas.
even_numbers_list = [x for x in range(1, 21)]
print(even_numbers_list)
even_numbers_list = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers_list)

#Desafio 2: Comprension de Diccionarios con Cadenas --> Crea un diccionarop a partir de una lista de palabras donde cada palabra sea una clave y su longitud sea el valor.
words = ["Python", "is", "wonderful", "and", "powerful"]
print(words)
word_lengths = {word: len(word) for word in words}
print(word_lengths)

#Desafio 3: Comprension de Listas Anidadas --> Genera una matriz de indentidad 3x3 usando comprension de listas anidadas (una matriz de identidad tiene 1s en la diagonal y 0s en otros lugares)
size = 3
identity_matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]
print(identity_matrix)

#Desafio 4: Procesamiento de Datos con "map()" y "filter()" --> Dada una lista de numeros, crea una nueva lista con cada numero al cuadrado y luego filtra los que sean mayores a 50.
numbers_list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers_list)
squared_filtered = list(filter(lambda x: x >= 50, map(lambda x: x**2, numbers_list)))
print(squared_filtered)

