from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.id'))
    friends = db.Column(db.String(80), unique=False)
    pending_friend_requests = db.Column(db.String(80), unique=False)
    sent_friend_requests = db.Column(db.String(80), unique=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    sunday= db.Column(db.String(80), unique=False, nullable=True)
    monday= db.Column(db.String(80), unique=False, nullable=True)
    tuesday= db.Column(db.String(80), unique=False, nullable=True)
    wednesday= db.Column(db.String(80), unique=False, nullable=True)
    thursday= db.Column(db.String(80), unique=False, nullable=True)
    friday= db.Column(db.String(80), unique=False, nullable=True)
    saturday= db.Column(db.String(80), unique=False, nullable=True)


    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "gym_id": self.gym_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "friends": self.friends,
            "pending_friend_requests": self.pending_friend_requests,
            "sent_friend_requests": self.sent_friend_requests,
            "is_active": self.is_active,
            "sunday": self.sunday,
            "monday": self.monday,
            "tuesday": self.tuesday,
            "wednesday": self.wednesday,
            "thursday": self.thursday,
            "friday": self.friday,
            "saturday": self.saturday
            
            
            # do not serialize the password, its a security breach
        }

class Posting(db.Model):
    __tablename__ = "posting"
    id = db.Column(db.Integer, primary_key=True)
    post_info = db.Column(db.String(80), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   

    def __repr__(self):
        return f'<Posting {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_info": self.post_info
            
            # do not serialize the password, its a security breach
        }

class Gym(db.Model):
    __tablename__ = "gym"
    id = db.Column(db.Integer, primary_key=True)
    gym_name = db.Column(db.String(30), unique = True, nullable= False)
    users = db.relationship('User', backref= 'gym')
    events = db.relationship('Event', backref = 'gym')

    def __repr__(self):
        return f'<Gym {self.gym_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "gym_name": self.gym_name,
            "users": self.users,
            "events": self.events
            
            # do not serialize the password, its a security breach
        }

class Event(db.Model):
    __tablename__= "event"
    id = db.Column(db.Integer, primary_key= True)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.id'))
    event_name = db.Column(db.String(80), unique=False, nullable=False)
    event_date = db.Column(db.Integer, unique=False, nullable=False)
    event_description = db.Column(db.String(80), unique=False, nullable=False)
    event_posts = db.relationship('Event_Posts', backref='event')

    def __repr__(self):
        return f'<Event {self.event_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "gym_id": self.gym_id,
            "event_name": self.event_name,
            "event_date": self.event_date,
            "event_description": self.event_descripiton
            
            # do not serialize the password, its a security breach
        }

class Event_Posts(db.Model):
    __tablename__ = "event_posts"
    id = db.Column(db.Integer, primary_key= True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    event_post_data = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<Event_Posts {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "event_post_data": self.event_post_data,
            "event_id": self.event_id
        }


    

