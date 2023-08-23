from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.hangman.hangman import HangmanGame
from app.hangman.words_list import get_random_words_list
from app.models import GameResult 

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'hangman_game' not in session:
        session['hangman_game'] = HangmanGame().to_dict()

    hangman_game_data = session['hangman_game']
    hangman_game = HangmanGame.from_dict(hangman_game_data)

    if request.method == 'POST':
        guess = request.form.get('guess', '').lower()

        if not guess.isalpha():
            flash('Please enter letters only.', 'danger')
        else:
            message = hangman_game.make_guess(guess)

            if hangman_game.is_game_over():
                if hangman_game.max_attempts <= 0:
                    flash('Game Over. You are out of attempts!', 'danger')
                    message = " Game Over."
                    return redirect(url_for('game_over'))  # Redirect to "game_over" route

                flash(message, 'info')

    session['hangman_game'] = hangman_game.to_dict()

    if hangman_game.has_won():
        flash("Congratulations! You've guessed the word: " + hangman_game.secret_word, 'success')
        return redirect(url_for('win')) 

    if hangman_game.is_game_over() and hangman_game.max_attempts <= 0:
        return redirect(url_for('game_over'))  

    current_word = hangman_game.display_word()
    guessed_letters = hangman_game.guesses
    secret_word = hangman_game.secret_word
    current_hangman_state = hangman_game.current_hangman_state  # Add this line

    return render_template('game.html', current_word=current_word, guessed_letters=guessed_letters, secret_word=secret_word, current_hangman_state=current_hangman_state)
