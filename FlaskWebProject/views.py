"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, jsonify, make_response, abort
from FlaskWebProject import app
from formula import *

@app.route('/')
@app.route('/home')
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