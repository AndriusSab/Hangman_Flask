
from sqlalchemy.orm import Session
from app.models import GameResult
from app import db
from random import choice



class GameResultsCrud:
    def __init__(self, db: Session):
        self.db = db

    def create_game_result(self, word, outcome, player_id):
        game_result = GameResult(
            word=word,
            outcome=outcome,
            player_id=player_id,
        )
        self.db.add(game_result)
        self.db.commit()
        return game_result.id

    def get_game_result_by_id(self, result_id):
        return self.db.query(GameResult).filter_by(id=result_id).first()

    def get_all_game_results(self):
        return self.db.query(GameResult).all()

    def update_game_result(self, result_id, new_outcome):
        game_result = self.get_game_result_by_id(result_id)
        game_result.outcome = new_outcome
        self.db.commit()
        return game_result

    def delete_game_result(self, game_result):
        self.db.delete(game_result)
        self.db.commit()

    def as_dict(self):
        return {
            "id": self.id,
            "word": self.word,
            "outcome": self.outcome,
            "player_id": self.player_id,
        }