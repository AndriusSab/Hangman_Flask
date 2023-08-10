# app/routes/results.py

from flask import render_template
from app import app
from app.models.player import Player

@app.route('/results')
def results():
    players = Player.query.all()
    return render_template('results.html', players=players)