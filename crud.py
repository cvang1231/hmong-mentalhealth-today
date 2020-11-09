"""CRUD operations."""

from model import db, User, Therapist, Favorite, connect_to_db


# Functions for user!


def create_user(email, password, zipcode):
    """Create and return a new user."""

    user = User(email=email, password=password, zipcode=zipcode)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users in database."""

    return User.query.all()


def get_user_by_id(user_id):
    """Return a user by their user_id."""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


# Functions for therapist!


def add_therapist(name, email, website, lat, long, specialty, img):
    """Create and return a new therapist."""

    therapist = Therapist(name=name, 
                        email=email,
                        clinic=clinic,
                        website=website,
                        lat=lat,
                        long=long,
                        specialty=specialty,
                        img=img
                        )

    db.session.add(therapist)
    db.session.commit()

    return therapist


def get_therapists():
    """Return all therapists in database."""

    return Therapist.query.all()


def get_therapist_by_id(therapist_id):
    """Return a therapist by their therapist_id."""

    return Therapist.query.filter(Therapist.therapist_id == therapist.id).first()


def get_therapist_by_email(email):
    """Return a therapist by email."""

    return Therapist.query.filter(Therapist.email == email).first()


# Function for favorite


def create_fav(user_id, therapistId):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, therapist_id=therapistId)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_fav_therapists(userId):
    """Return a user's favorite therapists."""

    list_of_therapists = []
    user_favs = Favorite.query.filter(Favorite.user_id == userId).all()

    for fav in user_favs:

        therapist = Therapist.query.filter(Therapist.therapist_id == therapist_id).all()

        list_of_therapists.append(therapist)

    return list_of_therapists


if __name__ == '__main__':
    from server import app
    connect_to_db(app)