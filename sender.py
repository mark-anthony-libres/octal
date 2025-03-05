from flask import Flask, request, render_template, url_for
import requests
import json, os
from dotenv import load_dotenv
load_dotenv()

host = os.getenv('HOST', '127.0.0.1') 
port = os.getenv('SENDER_PORT', 5000) 
receiver_port = os.getenv('RECEIVER_PORT', 8000)
output_filename = os.getenv('OUTPUT_FILENAME', 8000)

app = Flask(__name__)

@app.route("/sender", methods=['POST'])
def sender():
    data = request.get_json()
    content = data['data']

    # save to db to temporary file
    with open("output", "w") as file:
        file.write(content)

    return { "status" : "Success", "content" : content}

@app.route("/", methods=['GET'])
def display_sender():
    sender_url = url_for('sender')
    return render_template('./index.html', sender_url=sender_url, receiver_port = receiver_port)


if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)