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

    def __repr__(self):

        return f'<User user_id={self.user_id} email={self.email} zipcode={self.zipcode}>'

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)


class Therapist(db.Model):
    """A therapist."""

    __tablename__ = 'therapists'

    # primary key for therapists table
    thrpst_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    clinic = db.Column(db.String, nullable=False)
    website = db.Column(db.String)
    email = db.Column(db.String(50))
    specialty = db.Column(db.Text)
    lat = db.Column(db.Numeric(precision=9, scale=2), nullable=False)
    long = db.Column(db.Numeric(precision=9, scale=2), nullable=False)
    img = db.Column(db.String)
    county = db.Column(db.String)

    def __repr__(self):

        return f'<Therapist thrpst_id={self.thrpst_id} name={self.name} email={self.email} county={self.county}>'


class Favorite(db.Model):
    """A favorite."""

    __tablename__ = 'favorites'

    # primary key for favorites table
    fav_id = db.Column(db.Integer, primary_key=True, unique=True)
    # foreign key from users table
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    # foreign key from therapists table
    thrpst_id = db.Column(db.Integer, db.ForeignKey('therapists.thrpst_id'))

    user = db.relationship('User', backref='favorites')
    therapist = db.relationship('Therapist', backref='favorites')

    def __repr__(self):

        return f'<Favorite fav_id={self.fav_id} therapist_id={self.thrpst_id} user_id={self.user_id}>'




if __name__ == '__main__':
    from server import app

    connect_to_db(app)