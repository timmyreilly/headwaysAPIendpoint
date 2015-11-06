"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, jsonify, make_response, abort
from FlaskWebProject import app
from formula import *

@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
@app.route('/chitown/<int:distance>/<int:velocity>', methods=['GET'])
def get_wait(distance, velocity):
    wait = chi_town_wait(distance, velocity)
    return jsonify({'wait': wait})
    
@app.route('/float/<float:distance>/<float:velocity>', methods=['GET'])
def get_float(distance, velocity):
    wait = chi_town_wait(distance, velocity)
    return jsonify({'wait': wait})
    
# @app.route('/generic/<int:distance>/<int:velocity/<float:d>/<float:g>/<float:h>/', methods=['GET'])
# def get_generic(distance, velocity, d, g, h):
#     wait = whats_the_wait(distance, velocity, d, g, h)
#     return jsonify({'wait': wait})