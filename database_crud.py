from sqlalchemy.orm import Session
from app.models import GameResult
from app import db


class GameResultsCrud:
    def __init__(self, db: Session):
        self.db = db

    def create_game_result(self, word, outcome, player_id):
        try:
            game_result = GameResult(
                word=word,
                outcome=outcome,
                player_id=player_id,
            )
            self.db.add(game_result)
            self.db.commit()
            return game_result.id
        except Exception as e:
            self.db.rollback()
            raise e

    

    def as_dict(self, game_result):
        return {
            "id": game_result.id,
            "word": game_result.word,
            "outcome": game_result.outcome,
            "player_id": game_result.player_id,
        }
