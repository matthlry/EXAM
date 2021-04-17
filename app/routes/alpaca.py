from random import randint

from flask import request, jsonify

from app import app
from app.controller.alpaca_controller import alpaca_controller

@app.route('/')
def index(age = 0):
    return alpaca_controller.index(age)

# TODO: implement profile for each user
@app.route('/profile/<name>')
def profile(name):
    return alpaca_controller.profile(name)

# TODO: implement api