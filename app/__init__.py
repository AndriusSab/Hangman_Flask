from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.models.player import Player

app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

from app.models import player  # Import your Player model for session management

@login_manager.user_loader
def load_user(user_id):
    return Player.query.get(int(user_id))

# Import and register your route modules
from app.routes import game, login, player, results, registration

app.register_blueprint(game)
app.register_blueprint(login)
app.register_blueprint(player)
app.register_blueprint(results)
app.register_blueprint(registration)

# ... (other configurations and routes)

if __name__ == '__main__':
    app.run()
