"""Purpose: This module contains a simple script to practice and understand dictionaries.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-21"""

#Desafio 4: Crea un diccionario que represente un libro, incluyendo propiedades como título, autor y año. Agrega un nuevo par c;ave-valor, como el número de páginas. Actualiza el año edl libro. Elimin el autor del diccionario.

my_books_dictionary = {'title':'The Kybalion', 'author':'Hermes Trismegistus', 'year':1908 }
print(my_books_dictionary)
my_books_dictionary['page count'] = 171
print(my_books_dictionary)
my_books_dictionary['year'] = 1909
print(my_books_dictionary)
my_books_dictionary.pop('author')
print(my_books_dictionary)
