from app import db
from app.models import Player


class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.String(10), nullable=False)
    total_wins = db.Column(db.Integer, default=0)
    total_losses = db.Column(db.Integer, default=0)