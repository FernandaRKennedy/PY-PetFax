from petfax import create_app
from flask import Flask
app = Flask(__name__)

app = create_app()


@app.route('/')
def index():
    return 'Hello, PetFax!'


@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'
