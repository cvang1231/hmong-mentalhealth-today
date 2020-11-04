"""Models for Hmong for Mental Health Webapp"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        db.autoincrement=True,
                        db.primary_key=True)
    user_name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(20))
    zipcode = db.Column(db.Integer)

    def __repr__(self):

        return f'<User user_id={self.user_id} 
                user_name={self.user_name} 
                email={self.name}>'


class Therapist(db.Model):
    """A therapist."""

    __tablename__ = 'therapists'

    therapist_id = db.Column(db.Integer,
                        db.autoincrement=True,
                        db.primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    website = db.Column(db.String(200))
    lat_loc = db.Column(db.Integer)
    lon_loc = db.Column(db.Integer)
    speciality = db.Column(db.Text)
    img = db.Column(db.String)

    def __repr__(self):

        return f'<Therapist therapist_id={self.therapist_id} 
                name={self.name} 
                email={self.email}>'

def connect_to_db(flask_app, db_uri='postgresql:///hmongformentalhealth', echo=False):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)