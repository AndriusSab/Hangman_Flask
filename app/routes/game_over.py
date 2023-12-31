from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from app import app
from app.hangman.hangman import HangmanGame
from app.hangman.get_random_word import get_random_word

def reset_game_session():
    session.pop('hangman_game', None)

@app.route('/game_over', methods=['GET', 'POST'])
def game_over():
    secret_word = session['hangman_game']['secret_word']  
    reset_game_session()  

    if request.method == 'POST':
        return redirect(url_for('game'))  

    return render_template('game_over.html', secret_word=secret_word)