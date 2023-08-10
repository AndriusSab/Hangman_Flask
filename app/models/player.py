from app import db
from typing import Optional

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    game_results = db.relationship('GameResult', backref='player', lazy=True)

def get_player_by_id(player_id: int) -> Optional[Player]:
    return Player.query.get(player_id)

def create_player(username: str, email: str) -> Player:
    new_player = Player(username=username, email=email)
    db.session.add(new_player)
    db.session.commit()
    return new_player

def update_player(player: Player, new_username: Optional[str] = None, new_email: Optional[str] = None) -> None:
    if new_username:
        player.username = new_username
    if new_email:
        player.email = new_email
    db.session.commit()

def delete_player(player: Player) -> None:
    db.session.delete(player)
    db.session.commit()