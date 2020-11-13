"""Models for Hmong Mental Health Today Webapp"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_to_db(flask_app, db_uri='postgresql:///hmongmentalhealthtoday', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    # primary key for users table
    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.Integer)
    fav_id = db.Column(db.Integer, db.ForeignKey('favorites.fav_id'))

    def __repr__(self):

        return f'<User user_id={self.user_id} email={self.email} zipcode={self.zipcode}>'


class Therapist(db.Model):
    """A therapist."""

    __tablename__ = 'therapists'

    # primary key for therapists table
    therapist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    clinic = db.Column(db.String, nullable=False)
    website = db.Column(db.String)
    email = db.Column(db.String(50))
    specialty = db.Column(db.Text)
    img = db.Column(db.String)

    def __repr__(self):

        return f'<Therapist therapist_id={self.therapist_id} name={self.name} email={self.email}>'


class Favorite(db.Model):
    """A favorite."""

    __tablename__ = 'favorites'

    # primary key for favorites table
    fav_id = db.Column(db.Integer, primary_key=True)
    # foreign key from users table
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # foreign key from therapists table
    therapist_id = db.Column(db.Integer, db.ForeignKey('therapists.therapist_id'))

    #user = db.relationship('User', backref='favorites')

    def __repr__(self):
        return f'<Favorite fav_id={self.fav_id} therapist_id={self.therapist_id} user_id={self.user_id}>'



if __name__ == '__main__':
    from server import app

    connect_to_db(app)