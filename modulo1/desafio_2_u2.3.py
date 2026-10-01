
"""
Desafío 2: Modificador de Datos JSON
Lee un archivo JSON que contenga una lista de registros (diccionarios). Agrega un nuevo par clave-valor a cada registro y escribe los datos modificados en un nuevo archivo JSON.
Author: Edgar A. Barreiro Serrano, barreiro.edgar@gmail.com
Created: 2026-07-21 Modified: 2026-07-2
"""

import json

# Create data.json
sample_data = [{"name": "Alice", "age": 25},{"name": "Bob", "age": 30},{"name": "Charlie", "age": 28}]

with open("data.json", "w") as file:
    json.dump(sample_data, file, indent=4)

# Read data.json
with open('data.json', 'r') as file:
    data = json.load(file)

# Modify each record
for record in data:
    record['new_key'] = 'new_value'

# Write the modified data to a new file
with open('modified_data.json', 'w') as file:
    json.dump(data, file, indent=4)
