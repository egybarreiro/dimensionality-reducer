class HashTable:
    def __init__ (self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_index = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_index]):
            k, _ = kv
            if key == k:
                self.table[hash_index][i] = (key, value)
                return
        self.table[hash_index].append((key, value))

    def get(self, key):
        hash_index = self.hash_function(key)
        for k, v in self.table[hash_index]:
            if k == key:
                return v
        return None

# Probando la tabla hash
hash_table = HashTable()
hash_table.insert(10, 'apple')
hash_table.insert(20, 'banana')
hash_table.insert(10, 'grape')
print("Valor para clave 10:", hash_table.get(10))
print("Valor para clave 20:", hash_table.get(20))


"""
Desafío técnico 1: Sistema eficiente de recuperación de datos 
de usuarios.
Escenario:
Estás desarrollando una función para una aplicación de red social 
donde los usuarios pueden recuperar información de otros usuarios 
rápidamente, como su nombre de usuario y correo electrónico. 
Debido al alto volumen de solicitudes, el proceso de recuperación debe
ser muy eficiente.

Tarea:
Implementa un sistema de almacenamiento basado en hashing que permita
la recuperación rápida de información de usuarios basada en su ID de 
usuario único.

Instrucciones:
Crea una tabla hash para almacenar información de usuarios 
(ID de usuario, nombre de usuario, correo electrónico).
Implementa una función hash que distribuya eficientemente los IDs de 
usuario en la tabla hash.
Asegúrate de que tu sistema pueda manejar colisiones de forma adecuada.
Entrada:
Una lista de tuplas de información de usuario en el formato: 
(userID, username, email).
Ejemplo: [(123, "john_doe", "john@example.com"), (456, "jane_smith", 
"jane@example.com")]
Salida esperada:
Capacidad de recuperar la información de un usuario por su userID 
rápidamente.
Ejemplo: Para userID 123, el sistema debería devolver "john_doe", 
"john@example.com".
"""

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, name, email):
        hash_index = self.hash_function(key)
        for i, kv in enumerate(self.table[hash_index]):
            k, _ = kv
            if key == k:
                self.table[hash_index][i] = (key, name, email)
                return
        self.table[hash_index].append((key, name, email))

    def get(self, key):
        hash_index = self.hash_function(key)
        for k, name, email in self.table[hash_index]:
            if k == key:
                return name, email
        return None

# Probando la tabla hash
hash_table = HashTable()
hash_table.insert(123, "john_doe", "john@example.com")
hash_table.insert(456, "jane_smith", "jane@example.com")

#key = int(input("Entra el valor para traer el nombre e email: "))

#print("Valor para clave", key, ":", hash_table.get(key))


"""
Desafío técnico 2: detector de documentos duplicados
Escenario:
Tu empresa almacena miles de documentos y existe la posibilidad de 
documentos duplicados en el sistema. Se te encarga crear una 
herramienta que verifique duplicados de manera eficiente.

Tarea:
Diseña un algoritmo basado en hashing para detectar si existen 
documentos duplicados en el sistema.

Instrucciones:
Crea una función hash para generar un hash único para cada documento 
basado en su contenido. Compara los hashes para encontrar duplicados, 
asegurando que el proceso de comparación sea eficiente.
Entrada:
Una lista de documentos (cada documento es una cadena de texto).
Ejemplo: ["Document 1 text", "Document 2 text", "Document 1 text"]
Salida esperada:
Una lista o conjunto de documentos duplicados.
Ejemplo: En el ejemplo dado, la salida debería indicar que el primer y
tercer documento son duplicados.
"""

class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, document):
        # Genera un número basado en el contenido del documento
        return sum(ord(char) for char in document)

    def insert(self, document):
        key = self.hash_function(document)
        hash_index = key % self.size

        # Buscar si el documento ya existe
        for stored_key, stored_document in self.table[hash_index]:
            if stored_key == key and stored_document == document:
                return True  # Es duplicado

        # Si no existe, lo guardamos
        self.table[hash_index].append((key, document))
        return False


def find_duplicates(documents):
    hash_table = HashTable()
    duplicates = []

    for document in documents:
        if hash_table.insert(document) and document not in duplicates:
            duplicates.append(document)

    return duplicates


# Probando la tabla hash
documents = [
    "Document 1 text",
    "Document 2 text",
    "Document 1 text"
]

duplicates = find_duplicates(documents)

print("Documentos duplicados:")
for document in duplicates:
    print(document)


    """
    Desafío técnico 3: simulación de balanceador de carga
Escenario:
Estás trabajando en un balanceador de carga para un servidor web que 
distribuye solicitudes HTTP entrantes a diferentes servidores 
basándose en la ruta URL.

Tarea:
Implementa un algoritmo basado en hashing que asigne URLs entrantes 
a diferentes nodos de servidor y asegure una distribución uniforme de
solicitudes.

Instrucciones:
Simula un conjunto de servidores y asígnales un identificador único.
Desarrolla una función hash que mapee rutas URL a estos nodos de 
servidor. Asegura que el algoritmo distribuya las URLs lo más 
uniformemente posible entre los servidores.
Entrada:
Una lista de rutas URL.
Ejemplo: ["/home", "/about", "/contact", "/home", "/products"]
Salida esperada:
Un mapa de distribución mostrando qué URLs son manejadas por qué servidor.
Ejemplo: {"Servidor1": ["/home", "/about"], "Servidor2": ["/contact",
"/products"]}
"""

class LoadBalancer:
    def __init__(self, number_of_servers=3):
        self.number_of_servers = number_of_servers

        # Crear los servidores
        self.servers = {}

        for i in range(number_of_servers):
            server_name = "Servidor" + str(i + 1)
            self.servers[server_name] = []

    def hash_function(self, url):
        # Genera un número basado en los caracteres de la URL
        return sum(ord(char) for char in url)

    def assign_server(self, url):
        # Obtener el hash de la URL
        key = self.hash_function(url)

        # Determinar qué servidor manejará la URL
        server_index = key % self.number_of_servers

        server_name = "Servidor" + str(server_index + 1)

        # Guardar la URL en ese servidor
        self.servers[server_name].append(url)

        return server_name

    def get_distribution(self):
        return self.servers


# Probando el balanceador de carga
load_balancer = LoadBalancer(3)

urls = [
    "/home",
    "/about",
    "/contact",
    "/home",
    "/products",
    "/taquillas",
    "/tarjetas",
]

for url in urls:
    server = load_balancer.assign_server(url)
    print(url, "->", server)


print("\nDistribución de URLs:")
print(load_balancer.get_distribution())