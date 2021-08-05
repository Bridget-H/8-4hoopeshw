from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import posts
from app.models import posts
def post():
    form = posts()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        # once new_user is added to db, flash success message
        flash(f'Thank you for making a blog post! {new_user.username}!', 'secondary')

        #redirect user back to homepage
        return redirect(url_for('index'))
