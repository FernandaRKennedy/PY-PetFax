# config
from petfax import create_app
from flask import Flask
# config
from flask import Flask
app = Flask(__name__)

app = create_app()

# index route


@app.route('/')
def index():
    return 'Hello, PetFax!'

# pets index route


@app.route('/pets')
def pets():
    return 'These are our pets available for adoption!'
