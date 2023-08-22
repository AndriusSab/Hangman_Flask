from flask import render_template, request, redirect, url_for, flash
from app import app
from app.hangman.hangman import HangmanGame
from app.hangman.words_list import get_random_words_list

@app.route('/game', methods=['GET', 'POST'])
def game():
    hangman_game = HangmanGame()  
    current_word = hangman_game.secret_word
    print(current_word)
    guessed_letters = hangman_game.guesses
    print(guessed_letters)
    print(hangman_game.secret_word)
    if request.method == 'POST':
        guess = request.form.get('guess', '').lower()
        
        if not guess.isalpha():
            flash('Please enter letters only.', 'danger')
        elif len(guess) == 1:
            if guess in hangman_game.guesses:
                flash('You\'ve already guessed that letter.', 'info')
            elif guess in hangman_game.secret_word:
                hangman_game.make_guess(guess)
                flash('Correct guess! Keep it up!', 'success')
            else:
                hangman_game.make_guess(guess)
                flash('Incorrect guess! Try again', 'danger')
        elif len(guess) > 1:
            if guess == hangman_game.secret_word:
                hangman_game.make_guess(guess)
                flash(f'Congratulations! You\'ve guessed the word: {hangman_game.secret_word}', 'success')
            else:
                hangman_game.make_guess(guess)
                flash('Incorrect guess! Try again', 'danger')

        if hangman_game.is_game_over():
            flash('Game Over. You are out of attempts!', 'danger')
        

        

      
        return redirect(url_for('game'))
    
    return render_template('game.html', current_word = current_word, guessed_letters = guessed_letters)