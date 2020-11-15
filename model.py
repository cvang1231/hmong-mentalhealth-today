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
    #fav_id = db.Column(db.Integer, db.ForeignKey('favorites.fav_id'))

    # favorite = a list of Favorite objects

    def __repr__(self):

        return f'<User user_id={self.user_id} email={self.email} zipcode={self.zipcode}>'


class Therapist(db.Model):
    """A therapist."""

    __tablename__ = 'therapists'

    # primary key for therapists table
    thrpst_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    clinic = db.Column(db.String, nullable=False)
    website = db.Column(db.String)
    email = db.Column(db.String(50))
    specialty = db.Column(db.Text)
    lat = db.Column(db.Numeric(precision=9, scale=2), nullable=False)
    long = db.Column(db.Numeric(precision=9, scale=2), nullable=False)
    img = db.Column(db.String)

    def __repr__(self):

        return f'<Therapist thrpst_id={self.thrpst_id} name={self.name} email={self.email}>'


#class Favorite(db.Model):
 #   """A favorite therapist object."""

  #  __tablename__ = 'favorites'

    # primary key for favorites table
   # fav_id = db.Column(db.Integer, autoincrement=True primary_key=True)
    # foreign key from therapists table
    #thrpst_id = db.Column(db.Integer, db.ForeignKey('therapists.thrpst_id'))
    # foreign key from users table
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    #def __repr__(self) -> str:
     #   return f'<Favorite fav_id={self.fav_id} thrpst_id={self.thrpst_id} user_id={self.user_id}>'


#def example_data():

 #   User.query.delete()
  #  Therapist.query.delete()
   # Favorite.query.delete()

    #skip = User(
     #           user_id=20,
      #          email='skipskippy@test.com',
       #         password='skip1234',)
    #molly = User(
     #           user_id=70,
      #          email='mollym@test.com',
       #         password='molly1234')
    
    #mai = Therapist(
     #           thrpst_id=95,
      #          name='Mai Xiong Yang',
       #         clinic='Hennepin County',
        #        website='blahblahblah',
         #       email='maixy@test.com',
          #      specialty='my bio',)
    #tou = Therapist(
     #           therpst_id=110,
      #          name='Tou Vang',
       #         clinic='Fairview Hospital',
        #        website='blehblehbleh',
         #       email='touv@test.com',
          #      specialty='my bio',)

    #fav_1 = Favorite(
     #           fav_id=1,
      #          user_id=20,
       #         thrpst_id=95)
    #fav_2 = Favorite(
     #           fav_id=2,
      #          user_id=70,
           #     thrpst_id=110)



if __name__ == '__main__':
    from server import app

    connect_to_db(app)