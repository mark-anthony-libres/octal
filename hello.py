from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=['POST'])
def receiver():
    data = request.get_json()
    content = data['data']

    with open("output", "w") as file:
        file.write(content)

    return { "status" : "Success", "content" : content}


@app.route("/output", methods=['GET'])
def display():

    try:
        with open("output", "r") as file:
            content = file.read()
        return f"<pre>{content}</pre>" 
    except FileNotFoundError:
        return f"<h1>Error: The file output was not found.</h1>"
   

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)