from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    # Usando socketio.emit() para emitir para todos os clientes
    socketio.emit("message", msg)  # Correção aqui: broadcast é implicito em socketio.emit

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
