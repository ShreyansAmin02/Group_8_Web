from . import db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'  # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    # password is never stored in the DB, an encrypted password is stored
    # the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
    comments = db.relationship('Event', backref='user')


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    eventTitle = db.Column(db.String(80))
    artistName = db.Column(db.String(80))
    style = db.Column(db.String(80))
    address = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    startTime = db.Column(db.Time)
    endTime = db.Column(db.Time)
    image = db.Column(db.String(400))
    description = db.Column(db.String(400))
    tickets = db.Column(db.Integer)
    price = db.Column(db.Integer)
    status = db.Column(db.String(30)) # need to record either Open, Inactive, Cancelled, Sold Out
    contactDetails = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # ... Create the Comments db.relationship
    # relation to call event.comments and comment.event
    comments = db.relationship('Comment', backref='event')

    def __repr__(self):  # string print method
        return "<Name: {}>".format(self.name)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    def getNiceTime(self):
        return self.created_at.strftime("%d/%m/%y/%I:%M %p")

    def __repr__(self):
        return "<Comment: {}>".format(self.text)
    
class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(80))
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    Event.tickets = Event.tickets - amount
    