import datetime
from . import db

class User(db.Model):
    __tablename__ = 'users'

    # Change the column names as it matches your requirements
    # Keeping id as INT
    id = db.Column('id', db.Integer, primary_key = True)
    # Username cannot exceed 100 chars
    username = db.Column('name', db.String(100))
    created_on = db.Column('created_on', db.DateTime, default=datetime.utcnow)

    def __init__(self, username):
        self.username = username
