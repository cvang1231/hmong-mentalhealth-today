"""Server for Hmong Mental Health Today Webapp"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
import os

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')


######################## THERAPIST(S) ROUTES ########################
@app.route('/therapists')
def view_therapists():
    """View all therapists."""

    therapists = crud.get_therapists()

    return render_template('therapists.html', therapists=therapists)


@app.route('/therapists/<therapist_id>')
def therapist_details(therapist_id):
    """View details on a therapist."""

    therapist = crud.get_therapist_by_id(therapist_id)

    return render_template('therapist_details.html', therapist=therapist)


######################## FAVORITE ROUTES ########################
@app.route('/therapists/<therapist_id>/fav_therapist')
def add_therapist(therapist_id):
    """Add therapist to favorites."""

    therapistId = crud.get_therapist_by_id(therapist_id)
    session['therapist'] = therapist

    if session['user']:
        db_favorite = crud.create_fav(therapist)
        flash('Therapist favorited.')
    flash('Log in to see your favorite therapist(s).')

    return redirect('/')


######################## USER REGISTRATION AND LOGIN ROUTES ########################
#@app.route('/users')
#def all_users():
    #"""View all users."""

    #users = crud.get_users()

    #return render_template('all_users.html', users=users)


@app.route('/create_user', methods = ['POST'])
def register_user():
    """Creates a new user with given inputs."""

    email = request.form.get('email')
    password = request.form.get('password')
    zipcode = request.form.get('zipcode')

    user = crud.get_user_by_email(email)

    if user == None:
        crud.create_user(email, password, zipcode)
        flash('Account created! You can now login.')

        return redirect('/login')

    else:
        flash('Cannot create an account with existing email! Please try again.')

        return redirect('/')


@app.route('/login')
def log_in():
    """View login page."""

    return render_template('login.html')


@app.route('/handle_login', methods = ['POST'])
def handle_login():
    """Checks to see if password and email match with given inputs."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and user.password == password:
        session['user'] = user.user_id
        flash(f'Successfully logged in {email}')

        return redirect('/')

    else: 
        flash('Incorrect password and/or email. Please try again.')

        return redirect('/login')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)