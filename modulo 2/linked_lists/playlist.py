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