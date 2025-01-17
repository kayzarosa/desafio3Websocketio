from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("message")
def handle_message(msg):
    print(f"Mensagem lida: {msg}")
    emit("message", msg, broadcast=True)


# websockets
@socketio.on("connect")
def handle_connect():
    print("Client connected to the server")


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected to the server")


if __name__ == "__main__":
    socketio.run(app, debug=True)
