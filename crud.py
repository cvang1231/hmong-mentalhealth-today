"""CRUD operations."""

from model import db, User, Therapist, Favorite, connect_to_db


######################## Functions for user! ########################


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
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


######################## Functions for therapist! ########################


def add_therapist(name, clinic, website, email, specialty, img):
    """Create and return a new therapist."""

    therapist = Therapist(
                        name=name, 
                        clinic=clinic,
                        website=website,
                        email=email,
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
    """Return a therapist by primary key."""

    return Therapist.query.get(therapist_id)


def get_therapist_by_email(email):
    """Return a therapist by email."""

    return Therapist.query.filter(Therapist.email == email).first()


######################## Function for favorite ########################


def create_fav(user_id, therapist_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, therapist_id=therapist_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_user_favorites_by_id(fav_id):
    """Return a new user favorite."""

    return Favorite.query.get(fav_id)


def get_fav_therapists(userId):
    """Return a user's favorite therapists."""

    list_of_therapists = []
    user_favs = Favorite.query.filter(Favorite.user_id == userId).all()

    for fav in user_favs:

        therapist = Therapist.query.filter(Therapist.therapist_id == fav.therapist_id).all()

        list_of_therapists.append(therapist)

    return list_of_therapists


if __name__ == '__main__':
    from server import app
    connect_to_db(app)