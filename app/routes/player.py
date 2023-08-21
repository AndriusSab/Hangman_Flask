# app/routes/player.py

from flask import render_template, flash, redirect, url_for
from app.models.player import Player
from app import app, db

@app.route('/player/<int:player_id>')
def player_profile(player_id):
    player = Player.query.get(player_id)
    if player is None:
        flash('Player not found', 'danger')
        return redirect(url_for('index'))

    return render_template('player_profile.html', player=player)