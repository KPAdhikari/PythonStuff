from flask_login import UserMixin
from . import db
#######kp:
#
# The user model represents what it means for the app to have a user. This tutorial will require fields for an email address, password, and name. In future applications, you may decide you want much more information to be stored per user. You can add things like birthdays, profile pictures, locations, or any user preferences.

#Models created in Flask-SQLAlchemy are represented by classes that then translate to tables in a database. The attributes of those classes then turn into columns for those tables.

#We Define the User model as follows. This code defines a User with columns for an id, email, password, and name.

########kp:
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
