from typing import Container
from flask import Flask, render_template
from docker import DockerClient


client = DockerClient(base_url='unix://var/run/docker.sock')
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    data = {}
    containers = client.containers.list()
    data["containers"] = containers
    return render_template("index.html",
    data = data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")