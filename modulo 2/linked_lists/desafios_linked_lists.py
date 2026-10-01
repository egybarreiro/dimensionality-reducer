# Desafío 1

""" 
Desafío técnico 1: gestión de playlist con lista enlazada simple
Escenario:
Se te encarga desarrollar el backend de la función de playlist de una 
app de música. La app debe permitir a los usuarios añadir canciones al 
final de su lista de reproducción y pasar a la siguiente canción.

Tarea:
Implementa una lista enlazada simple para gestionar las canciones en la 
playlist de un usuario. La lista debe permitir añadir canciones al final 
y obtener la siguiente canción a reproducir.

Entrada:
Operaciones a realizar en la playlist, como "agregar canción" y 
"reproducir siguiente".
Ejemplo de entradas: add_song("Yesterday"), add_song("Hey Jude"), 
play_next(), add_song("Let it Be"), play_next()
Salida esperada:
La canción actual que se está reproduciendo después de cada operación.
Para el ejemplo dado, las salidas serían "Canción agregada: Yesterday", 
"Canción agregada: Hey Jude", "Reproduciendo ahora: Yesterday", 
"Canción agregada: Let it Be", "Reproduciendo ahora: Hey Jude".
"""

# Definiendo las clases y funciones para SLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_song(self, song):
        new_node = Node(song)

        # If the playlist is empty
        if self.head is None:
            self.head = new_node
        else:
            # Find the last song
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

        print("Canción agregada:", song)

    def play_next(self):
        # If the playlist is empty
        if self.head is None:
            print("La playlist está vacía.")
            return None

        # Get the first song
        song = self.head.data

        # Remove it from the playlist
        self.head = self.head.next

        print("Reproduciendo ahora:", song)

        return song

    def traverse(self):
        if self.head is None:
            print("La playlist está vacía.")
            return

        current = self.head

        print("Playlist:")

        while current:
            print("-", current.data)
            current = current.next

    def get_songs(self):
        songs = []

        current = self.head

        while current:
            songs.append(current.data)
            current = current.next

        return songs


# Bloque del main para que corra el playlist
from flask import Flask, render_template, request, redirect, url_for
from playlist import SinglyLinkedList


app = Flask(__name__)


# Create the playlist
playlist = SinglyLinkedList()

# Keep track of the current song
current_song = None


@app.route("/")
def home():
    return render_template(
        "index.html",
        songs=playlist.get_songs(),
        current_song=current_song
    )


@app.route("/add", methods=["POST"])
def add_song():
    song = request.form["song"]

    playlist.add_song(song)

    return redirect(url_for("home"))


@app.route("/play")
def play_next():
    global current_song

    current_song = playlist.play_next()

    return redirect(url_for("home"))


@app.route("/clear")
def clear_playlist():
    global current_song

    playlist.head = None
    current_song = None

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)



#Desafío 2
"""
Desafío técnico 2: Historial del navegador usando lista 
enlazada doble.
Escenario:
Estás desarrollando un navegador web y necesitas implementar una 
función para gestionar el historial del usuario, permitiéndole 
ir hacia atrás y hacia adelante entre páginas visitadas.

Tarea:
Usa una lista enlazada doble para registrar las páginas visitadas 
por el usuario. Cada nodo debe representar una página web. 
Implementa funciones para ir hacia atrás y hacia adelante en el
historial.

Entrada:
Una serie de visitas a páginas web y acciones de navegación, 
como "visitar página", "ir atrás" e "ir adelante".
Ejemplo de entradas: visit("page1.com"), visit("page2.com"), 
go_back(), go_forward(), visit("page3.com"), go_back()

Salida esperada:
La página actual después de cada operación.
Para el ejemplo dado, las salidas serían "Página actual: 
page1.com", "Página actual: page2.com", "Regreso a: page1.com", 
"Avance a: page2.com", "Página actual: page3.com", "Regreso a: 
page2.com".
"""

# Definiendo las clases y funciones para DLL
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self):
        self.current = None

    def visit(self, url):
        new_node = DoubleNode(url)
        if self.current is None:
            self.current = new_node
        else:

            if self.current.next:
                self.current.next.prev = None
                self.current.next = None

            self.current.next = new_node
            new_node.prev = self.current
            new_node.next = None

            self.current = new_node

    def go_back(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

    def go_forward(self):
        if self.current and self.next:
            self.current = self.next

    def get_current_page(self):
        if self.current:
            return self.current.data
        return None

    def print_current_page(self):
        if self.current:
            print(self.current.data)
        else:
            print("Historial vacío.")

    def traverse_forward_from_current(self):
        node = self.current
        print("Recorrido hacia adelante desde current:")
        while node:
            print(" ->", node.data)
            node = node.next

    def traverse_backward_from_current(self):
        node = self.current
        print("Recorrido hacia atrás desde current:")
        while node:
            print(" <-", node.data)
            node = node.prev


# "Main" para corrida de prueba

if __name__ == "__main__":
    history = BrowserHistory()

    history.visit("page1.com")
    history.print_current_page()

    history.visit("page2.com")
    history.print_current_page()

    history.go_back()
    history.print_current_page()

    history.go_forward()
    history.print_current_page()

    history.visit("page3.com")
    history.print_current_page()

    history.go_back()
    history.print_current_page()



"""
Desafío técnico 3: Cola personalizada para tickets de servicio 
al cliente.
Escenario:
Tu empresa está desarrollando un sistema de tickets de servicio 
al cliente. Cada ticket tiene un ID único y un nivel de prioridad.

Tarea:
Implementa un sistema de cola donde los tickets se procesan 
según su orden de llegada. Sin embargo, los tickets de alta 
prioridad (prioridad 1) deben procesarse antes que los de menor 
prioridad.

Entrada:
IDs de tickets y sus niveles de prioridad.
Ejemplo de entradas: add_ticket(101, 2), add_ticket(102, 1), 
add_ticket(103, 3), process_ticket(), add_ticket(104, 1), 
process_ticket().
Salida esperada:
El ID del ticket que se está procesando después de cada operación.
Para el ejemplo dado, las salidas serían "Ticket 101 agregado", 
"Ticket de alta prioridad 102 agregado", "Ticket 103 agregado",
"Procesando ticket: 102", "Ticket de alta prioridad 104 agregado", 
"Procesando ticket: 101".
"""

#Definiendo las clases con funciones.
from collections import deque

class Ticket:
    def __init__(self, ticket_id, priority):
        self.ticket_id = ticket_id
        self.priority = priority

class TicketQueue:
    def __init__(self):
        self.high_priority = deque()
        self.normal_priority = deque()

    def add_ticket(self, ticket_id, priority):
        ticket = Ticket(ticket_id, priority)

        if priority == 1:
            self.high_priority.append(ticket)
            print(f"Ticket {ticket_id} agregado.")
        else:
            self.normal_priority.append(ticket)
            print(f"Ticket {ticket_id} agregado.")

    def process_ticket(self):
        if self.high_priority:
            ticket = self.high_priority.popleft()
            print(f"Procesando ticket: {ticket.ticket_id}")
        elif self.normal_priority:
            self.normal_priority.popleft()
        else:
            print("No hay tickets para procesar.")


#"Main" para corrida de prueba.
if __name__ == "__main__":
    queue = TicketQueue()

    queue.add_ticket(101, 2)
    queue.add_ticket(102, 1)
    queue.add_ticket(103, 3)
    queue.process_ticket()
    queue.add_ticket(104, 1)
    queue.process_ticket()
