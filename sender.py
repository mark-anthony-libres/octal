from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sender():
    data = request.form
    response = requests.post(
        'http://127.0.0.1:8000',
        headers={'Content-Type': 'application/json'},
        json=dict(data)
    )

    print("Response from the receiver server:", response.json())
    return data