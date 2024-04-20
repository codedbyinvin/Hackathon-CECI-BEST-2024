
from flask import Flask

app = Flask(__name__)


# import hello_world from the hello_world.py
from hello_world import hello_world


@app.route('/')
def hello():
    return hello_world()