import datetime
from . import db
import enum


'''
Defines player primary account details.
This table contains all the game related stuff.
'''
class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    
    def __init__(self, email, name, status):
        self.email = email
        self.name = name
        self.status = status


'''
Role of a player in the world of Risgard

Administrator: Access to Administration panel
Moderator: Authority to ban misbehaving players or
Influencer: Ability to elect or impeach Moderators
Commoner: Normal players, no rights in the development of game or platform
'''
class UserAuthLevel(enum.Enum):
    Commoner = 1
    Influencer = 2
    Moderator = 3
    Administrator = 4


'''
Defines a user acccount
@params: 
    email: The email id of the User.
    bio: Bio text, normally a long text set by the user, that acts as an introduction.
    flavor_text: Stores the moto of the player, a small witty one-liner to impress your compatriots.
'''
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column('id', db.Integer, primary_key=True)
    email = db.Column('email', db.Integer, primary_key=True)
    bio = db.Column('bio', db.String(250))
    role = db.Column('role', db.Enum(UserAuthLevel), default=4)
    flavor_text = db.Column('flavor_text', db.String(50))
    created_on = db.Column('created_on', db.DateTime, default=datetime.utcnow)

    def __init__(self, email, bio='', flavor_text=''):
        self.email = email
        self.bio = bio
        self.flavor_text = flavor_text


'''
Skills available in the game
@params:
	
'''
class Skill(db.Model):
    __tablename__ = 'skills'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), primary_key=True)
    desc = db.Column('desc', db.String(100))
    nxt_skill = db.Column('nxt_skill', db.Integer)
    max_lvl = db.Column('max_lvl', db.Integer)

    def __init__(self, name, desc, nxt_skill, max_lvl):
        self.name = name
        self.desc = desc
        self.nxt_skill = nxt_skill
        self.max_lvl = max_lvl


'''
Classes a player can belong to in this game
'''
class Class(db.Model):
    __tablename__ = 'classes'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), primary_key=True)
    desc = db.Column('desc', db.String(100))
    nxt_stage = db.Column('nxt_stage', db.Integer)
    points_req = db.Column('points_req', db.Integer)
    skill = db.Column('skill', db.Integer)

    def __init__(self, name, desc, nxt_stage, points_req, skill):
        self.name = name
        self.desc = desc
        self.nxt_stage = nxt_stage
        self.points_req = points_req
        self.skill = skill


'''
Information about all the game items
'''
class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(50), primary_key=True)
    desc = db.Column('desc', db.String(100))

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


'''
Code snippets executed via Exec API
'''
class Snippet(db.Model):
    __tablename__ = 'snippets'

    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('id', db.Integer)
    body = db.Column('body', db.String)

    def __init__(self, body, user_id):
        self.body = body
        self.user_id = user_id


'''
Types of location available in the game 
'''
class LocationType(enum.Enum):
    City = 1
    Village = 2
    Unknown = 4


'''
Places available in the map
'''
class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column('id', db.Integer, primary_key=True)
    coord = db.Column('coord', db.String, primary_key=True)
    loc_type = db.Column('type', db.Enum(LocationType), default=4)
    name = db.Column('name', db.String(50), primary_key=True)
    desc = db.Column('desc', db.String)

    def __init__(self, coord, loc_type, name, desc):
        self.coord = coord
        self.loc_type = loc_type
        self.name = name
        self.desc = desc