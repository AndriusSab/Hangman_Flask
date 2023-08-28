from app import db
from sqlalchemy.orm import relationship


class GameResult(db.Model):
    __tablename__ = "GameResult"
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.String(10), nullable=False)
    total_wins = db.Column(db.Integer, default=0)
    total_losses = db.Column(db.Integer, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('Player.id'))
    player = relationship("Player", back_populates="game_results")
    
