from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"<h1>Week 3 Docker App </h1><p>Container Hostname: {hostname}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
