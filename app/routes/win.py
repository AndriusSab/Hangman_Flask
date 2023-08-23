from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from app import app
from app.hangman.hangman import HangmanGame


def reset_game_session():
    session.pop('hangman_game', None)

@app.route('/win', methods=['GET', 'POST'])
def win():
    secret_word = session['hangman_game']['secret_word']  # Get the secret word from the current game
    reset_game_session()  # Reset the game session

    if request.method == 'POST':
        return redirect(url_for('game'))  # Redirect to the game page to start a new game

    return render_template('win.html', secret_word=secret_word)
