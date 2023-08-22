from flask import render_template, redirect, url_for, flash, session
from app import app, db
from app.forms.login import LoginForm
from app.models.player import Player

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        player = Player.query.filter_by(email=email).first()

        if player and player.check_password(password):
            session['user_id'] = player.id
            flash('Logged in successfully!', 'success')
            return redirect(url_for('game'))  # Redirect to the "game" route

        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)
