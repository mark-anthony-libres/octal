from flask import Flask, request, render_template
import requests, os
from flask_socketio import SocketIO, send
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('HOST', '127.0.0.1') 
port = os.getenv('RECEIVER_PORT', 8000) 

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/", methods=['GET'])
def display():

    try:
        with open("output", "r") as file:
            content = file.read()
        return render_template('./display.html', message=content)
    except FileNotFoundError:
        return f"<h1>Error: The file output was not found.</h1>"



@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    send(msg, broadcast=True)


if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)