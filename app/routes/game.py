from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.hangman.hangman import HangmanGame
from database_crud import GameResultsCrud  
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')




@app.route('/game', methods=['GET', 'POST'])
def game():
    logging.info('Game route accessed.')
    
    if 'hangman_game' not in session:
        session['hangman_game'] = HangmanGame().to_dict()

    hangman_game_data = session['hangman_game']
    hangman_game = HangmanGame.from_dict(hangman_game_data)

    if request.method == 'POST':
        guess = request.form.get('guess', '').lower()
        logging.debug('Received guess: %s', guess)

        if not guess.isalpha():
            flash('Please enter letters only.', 'danger')
        else:
            message = hangman_game.make_guess(guess)
            flash(message, 'info')
                              

    session['hangman_game'] = hangman_game.to_dict()
    logging.debug('Session updated with hangman game data.')

    if hangman_game.has_won():
        logging.info('Player won the game.')
        flash("Congratulations! You've guessed the word: " + hangman_game.secret_word, 'success')
        player_id = 1 # need to
        outcome = "win"
        crud = GameResultsCrud(db.session)
        crud.create_game_result(hangman_game.secret_word, outcome, player_id)
        return redirect(url_for('win'))

    if hangman_game.is_game_over():
        
        logging.info('Player lost the game.')
        flash('Game Over. You are out of attempts!', 'danger')
        player_id = 1 
        outcome = "lost"
        crud = GameResultsCrud(db.session)
        crud.create_game_result(hangman_game.secret_word, outcome, player_id)
        return redirect(url_for('game_over'))
    

    current_word = hangman_game.display_word()
    guessed_letters = hangman_game.guesses
    secret_word = hangman_game.secret_word
    current_hangman_state = hangman_game.current_hangman_state

    return render_template('game.html', current_word=current_word, guessed_letters=guessed_letters, secret_word=secret_word, current_hangman_state=current_hangman_state)