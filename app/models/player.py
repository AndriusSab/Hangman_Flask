from typing import Optional
from sqlalchemy.orm import relationship
from app import db

class Player(db.Model):
    __tablename__ = "Player"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128))  
    game_results = relationship("GameResult", back_populates="player")
    
    def set_password(self, password):
        self.password = password  

    def check_password(self, password):
        return self.password == password 

def get_player_by_id(player_id: int) -> Optional[Player]:
    return Player.query.get(player_id)

def create_player(username: str, email: str, password: str) -> Player:
    new_player = Player(username=username, email=email)
    new_player.set_password(password) 
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
