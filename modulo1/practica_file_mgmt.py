'''This is a File Management practice.'''

#Leer de un Archivo
content = file.read()
print(content)
file.close()

#Escribiendo en un archivo
file = open('example.txt', 'w')
file.write('Hello, Python!')
file.close()

   #Abriendo archivos con la declaracion with
with open('exampple.txt', 'r') as file:
    content = file.read()
    print(content)

#Trabajando en Archivos de Texto Plano
    #Leyendo un Archivo de Texto
    with open('example.txt', 'r') as file:
        for line in file:
            print(line, end='')

    #Escribiendo un Archivo de Texto
    with open('example.txt', 'w') as file:
        file.write('Escrinbiendo en un archivo de texto.n')
        file.write('Agregando otra linea')


#Trabajando en Archivos CSV
#import csv
with open('example.csv', 'r') as file: 
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

#Escribiendo en Archivo CSV
with open('example.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Nombre', 'Edad'])
    csv_writer.writerow(['Alice', '23'])
    csv_writer.writerow(['Bob', '30'])


#Trabajando con Archivos JSON
#import json
with open('example.json', 'r') as file:
    data = json.load(file)
    print(data)

#Escribiendo en Archivos JSON
data = {'name':'Alice', 'age':'23', 'city':'New York'}

with open('example.json', 'w') as file:
    json.dump(data, file)

   

 