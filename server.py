"""Server for Hmong Mental Health Today Webapp"""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def get_homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/therapists')
def view_therapists():
    """View all therapists."""

    therapists = crud.get_therapists()

    return render_template('therapists.html', therapists=therapists)

@app.route('/therapists/<therapist_id>')
def view_one_therapist(therapist_id):
    """View details on a therapist."""

    therapists = crud.get_therapist_by_id()

    return render_template('therapist_details.html', therapist=therapist)

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)