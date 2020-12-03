"""Server for Hmong Mental Health Today Webapp"""

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
from model import connect_to_db
import crud, json
import os


from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)


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
@login_required
def fav_therapist(thrpst_id):
    """Add therapist to favorites."""

    # This works on the Click to favorite button on therapist_details page

    favorite = crud.get_fav(current_user.get_id(), thrpst_id)

    # if current user is logged in
    if current_user.is_authenticated:

        # if user and therapist pairing not in db, create fav
        if not favorite:
            crud.create_fav(current_user.get_id(), thrpst_id)
            flash('Added to list of favorites.')

        else:
            flash('Therapist already favorited.')

    else:
        flash('Please login to favorite a therapist.')

    #user_id = session['user_id']

    # try seeing if user and therapist pairing are in database
    #try:
        #favorite = crud.get_fav(user_id, thrpst_id)
        # if not in database
        #if not favorite:
            # create user and therapist pairing
            #crud.create_fav(user_id, thrpst_id)
            #flash('You just added this therapist as a favorite.')
        #else:
            #flash('Therapist already favorited.')
    # this code is executed if exception is raised in try block
    # if user_id not present, flash message will execute
    #except Unauthorized:
        #flash('Please log in to favorite a therapist.')

    return redirect(f'/therapists/{ thrpst_id }')


    #if session['user_id']:
        #crud.create_fav(session['user_id'], thrpst_id)
        #flash('Therapist favorited.')
        #return redirect (f'/therapists/{ thrpst_id }')

        #if session['user_id'] == None:
            #flash('Log in to favorite a therapist.')
            #return redirect(f'/therapists/{ thrpst_id }')


@app.route('/delete_favorite', methods=['POST'])
def delete_favorite():
    """Delete favorite from database."""

    # TODO: THIS NEEDS WORK. ASK FOR HELP.

    user_id = session['user_id']
    thrpst_id = request.form.get('therapist_name')
    favorite = crud.get_fav(user_id, thrpst_id)

    db.session.delete(favorite)
    db.session.commit()


######################## USER REGISTRATION AND LOGIN ROUTES ########################
@app.route('/create_account', methods = ['GET', 'POST'])
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

    user = crud.get_user_by_id(current_user.get_id())

    if current_user.is_authenticated:
        
        list_favs = crud.get_fav_therapists_name_by_id(current_user.get_id())
        print(list_favs)
        print(type(list_favs))
        print("-----------------")
        return render_template('user_details.html', user=user, list_favs=list_favs)
    else:
        flash('Please login to view your details.')
        return redirect('/login')


@app.route('/login')
def log_in():
    """Redirect user to login page when LOG IN button is clicked."""

    return render_template('login.html')


@login_manager.user_loader
def load_user(user_id):
    """Used to reload user object form user ID stored in session."""

    return crud.get_user_by_id(user_id)


@app.route('/handle_login', methods = ['POST'])
def handle_login():
    """Checks to see if email and password match with given inputs."""
    # This is the page where user logs in with their email and pw

    email = request.form.get('email')
    user = crud.get_user_by_email(email)

    if user:
        login_user(user)
        flash(f'Logged in successfully.')
        return redirect('/user/<user_id>')
    else:
        flash(f'Incorrect email or password. Try again.')
        return redirect('/login')

        # is_safe_url should check if the url is safe

    #if user and user.password == password:
        #session['user_id'] = user.user_id
        #flash(f'Successfully logged in {email}')

        #return redirect('/user/<user_id>')

    #else: 
        #flash('Incorrect password and/or email. Please try again.')

        #return redirect('/login')


@app.route('/logout')
@login_required
def logout():
    """Logs out user."""

    logout_user()
    return redirect('/')

    #del session['user_id']
    #flash('Logged out sucessfully.')
    #return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)