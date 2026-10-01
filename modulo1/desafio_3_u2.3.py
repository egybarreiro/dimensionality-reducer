'''Desafío 3: Calculadora de Promedios con CSV

Crea un archivo llamado grades.csv que contenga el nombre de tres estudiantes y sus tres calificaciones. Luego, lee el archivo, calcula el promedio de cada estudiante y guarda los resultados en un nuevo archivo llamado averages.csv.
Nombre, edad, y 3 calificaciones'''

import csv

# Create grades.csv
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Nota1", "Nota2", "Nota3"])
    writer.writerow(["Ana", 12, 90, 85, 95])
    writer.writerow(["Luis", 13, 80, 75, 70])
    writer.writerow(["María", 14, 100, 95, 98])

# Leer el archivo grades.csv
students = []
with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    averages = []
    for row in reader:
        name = row[0]
        grade1 = int(row[1])
        grade2 = int(row[2])
        grade3 = int(row[3])

        average = round((grade1 + grade2 + grade3) / 3,2)
        averages.append([name, average])

# Escribir el archivo averages.csv
with open("averages.csv", "w", newline="", encoding="utf-8") as file:
    fields = [column.upper() for column in ["name", "age", "average"]]
    writer = csv.writer(file)
   


