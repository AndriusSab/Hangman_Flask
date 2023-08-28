from flask import render_template
from app import app, db
from app.models import GameResult

@app.route('/results', methods=['GET'])
def results():
    results = GameResult.query.all()
    return render_template('results.html', results=results)
