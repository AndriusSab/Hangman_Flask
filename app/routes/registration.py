from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.registration import RegistrationForm
from app.models.player import Player

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_player = Player(username=form.username.data, email=form.email.data)
        new_player.set_password(form.password.data)
        db.session.add(new_player)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))  
    return render_template('registration.html', form=form)