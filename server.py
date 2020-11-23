"""Server for Hmong Mental Health Today Webapp"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from model import connect_to_db
import crud, json
import os


from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
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


@app.route('/therapists/dakota-county')
def therapist_by_dakota_county():
    """View all therapists by county."""

    therapists = crud.get_therapists()

    return render_template('dakota.html', therapists=therapists)


@app.route('/therapists/hennepin-county')
def therapist_by_hennepin_county():
    """View all therapists by county."""

    therapists = crud.get_therapists()

    return render_template('hennepin.html', therapists=therapists)


@app.route('/therapists/ramsey-county')
def therapist_by_ramsey_county():
    """View all therapists by county."""

    therapists = crud.get_therapists()

    return render_template('ramsey.html', therapists=therapists)


@app.route('/therapists/washington-county')
def therapist_by_washington_county():
    """View all therapists by county."""

    therapists = crud.get_therapists()

    return render_template('washington.html', therapists=therapists)


@app.route('/therapists/<thrpst_id>')
def therapist_details(thrpst_id):
    """View details on a therapist."""

    therapist = crud.get_therapist_by_id(thrpst_id)

    return render_template('therapist_details.html', therapist=therapist)


######################## FAVORITE LISTS ROUTES ########################
@app.route('/therapists/<thrpst_id>/fav-therapist', methods = ['POST'])
def fav_therapist(thrpst_id):
    """Add therapist to favorites."""

    # This works on the Click to favorite button on therapist_details page
    # TODO: WRITE CODE LETTING USER KNOW THEY CAN'T ADD SAME THERAPIST

    if session['user_id']:
        crud.create_fav(session['user_id'], thrpst_id)
        flash('Therapist favorited.')
        return redirect (f'/therapists/{ thrpst_id }')
    else:
        flash('Log in to see your favorite therapist(s).')
        return redirect('/')


@app.route('/delete_favorite', methods=['POST'])
def delete_favorite():
    """Delete favorite from database."""

    # Use fav_id to call favorite
    fav_id = request.form.get('favorite')
    favorite = crud.Favorite.query.get(fav_id)

    db.session.delete(favorite)
    db.session.commit()

    return flash('Deleted.')


######################## USER REGISTRATION AND LOGIN ROUTES ########################
@app.route('/create_user', methods = ['GET', 'POST'])
def register_user():
    """Creates a new user with given inputs."""

    email = request.form.get('email')
    password = request.form.get('password')
    zipcode = request.form.get('zipcode')

    user = crud.get_user_by_email(email)

    if user == None:
        new_user = crud.create_user(email, password, zipcode)
        flash('Account created! You can now login.')

        return redirect('/login')

    else:
        flash('Cannot create an account with existing email! Please try again.')

        return redirect('/')


@app.route('/user/<user_id>')
def user_details(user_id):
    """View details page for a particular user."""

    user_id = session.get('user_id')

    if user_id:
        user = crud.get_user_by_id(user_id)
        joined_fav = crud.get_fav_therapists_name_by_id(user_id)
        print(joined_fav)
        print(type(user))
        print("-----------------")
        return render_template('user_details.html', user=user, joined_fav=joined_fav)
    else:
        flash('Please login to view your details.')
        return redirect('/login')


@app.route('/login')
def log_in():
    """Redirect user to login page when LOG IN button is clicked."""

    return render_template('login.html')


@app.route('/handle_login', methods = ['POST'])
def handle_login():
    """Checks to see if email and password match with given inputs."""
    # This is the page where user logs in with their email and pw

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if user and user.password == password:
        session['user_id'] = user.user_id
        flash(f'Successfully logged in {email}')

        return redirect('/')

    else: 
        flash('Incorrect password and/or email. Please try again.')

        return redirect('/login')


@app.route('/log_out')
def log_user_out():
    del session['user_id']

    return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)