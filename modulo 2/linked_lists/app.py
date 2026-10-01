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