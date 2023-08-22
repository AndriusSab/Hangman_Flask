from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)


app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hangman.db'


db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.models.player import Player

@login_manager.user_loader
def load_user(user_id):
    return Player.query.get(int(user_id))

from app.models.player import Player
from app.models.game_result import GameResult

from app.routes.index import *
from app.routes.login import *
from app.routes.game import *
from app.routes.registration import *
from app.routes.results import *
from app.routes.player import *

