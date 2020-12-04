"""CRUD operations."""

from model import db, User, Therapist, Favorite, connect_to_db


######################## Functions for user! ########################
def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

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


def get_therapist_by_id(thrpst_id):
    """Return a therapist by primary key."""

    return Therapist.query.get(thrpst_id)


######################## Functions for favs! ########################   
def create_fav(user_id, thrpst_id):
    """Create and return a new favorite."""

    favorite = Favorite(user_id=user_id, thrpst_id=thrpst_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite


def get_fav(user_id, thrpst_id):
    """Return a favorite by user id and thrpst id."""

    return Favorite.query.filter_by(user_id=user_id, thrpst_id=thrpst_id).all()


def get_favorites_by_id(fav_id):
    """Return favorite pair by primary."""

    return Favorite.query.get(fav_id)


def get_fav_therapists_name_by_id(user_id):
    """Return a user's favorite therapists."""
    
    list_favs = []

    # get all Favorite.thrpst_id from a user
    thrpsts = db.session.query(Favorite.thrpst_id).filter_by(user_id=user_id)

    # loop through each Favorite.thrpst_id
    for therapist in thrpsts:
        # Grab Therapist.name from each Favorite.thrpst_id and append to list_favs
        list_favs.append(db.session.query(Therapist.name).filter_by(thrpst_id=therapist.thrpst_id).all())

    remove_syntax = ["[", "(", "'", "'", "," ")", "]"]
    fav_str = repr(list_favs)

    for syntax in remove_syntax:
        fav_str = fav_str.replace(syntax, '')
    
    list_favs = fav_str.split(",")

    if list_favs == ['']:
        return f'List is empty.'
    else:
        return list_favs




if __name__ == '__main__':
    from server import app
    connect_to_db(app)