"""CRUD operations."""

from model import db, User, Therapist, Favorite, connect_to_db


######################## Functions for user! ########################
def create_user(email, password, zipcode):
    """Create and return a new user."""

    user = User(email=email, password=password, zipcode=zipcode)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_user_details(email):
    """Return a user's details."""

    user = User.query.filter_by(email=email).first()
    user_pw = user.password
    user_id = user.user_id

    return user_pw, user_id

    
def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


######################## Functions for therapist! ########################
def create_therapist(name, clinic, website, email, specialty, lat, long, img, county):
    """Create and return a new therapist."""

    therapist = Therapist(
                        name=name, 
                        clinic=clinic,
                        website=website,
                        email=email,
                        specialty=specialty,
                        lat=lat,
                        long=long,
                        img=img,
                        county=county
                        )

    db.session.add(therapist)
    db.session.commit()

    return therapist


def get_therapists():
    """Return all therapists in database."""

    return Therapist.query.all()


def get_therapist_by_email(email):
    """Return a therapist by email."""

    return Therapist.query.filter(Therapist.email == email).first()


def get_therapist_by_county(county):
    """Return therapist by county."""

    return Therapist.query.filter(Therapist.county == county).all()


def get_therapist_by_id(thrpst_id):
    """Return a therapist by primary key."""

    return Therapist.query.get(thrpst_id)


######################## Functions for lists! ########################   
def create_fav(user_id, thrpst_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, thrpst_id=thrpst_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_user_favorites_by_id(fav_id):
    """Return a new user favorite."""

    return Favorite.query.get(fav_id)


def get_fav_therapists(user_id):
    """Return a user's favorite therapists."""

    list_therapists = []
    user_favs = Favorite.query.filter(Favorite.user_id == user_id).all()

    for fav in user_favs:

        therapist = Therapist.query.filter(Therapist.thrpst_id == fav.thrpst_id).all()

        list_therapists.append(therapist)

    return list_therapists




if __name__ == '__main__':
    from server import app
    connect_to_db(app)