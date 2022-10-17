from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    gym: map[list["Posting"]] = db.relationship(back_populates="parent")
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.id'))
    friends = db.Column(db.String(80), unique=False)
    pending_friend_requests = db.Column(db.String(80), unique=False)
    sent_friend_requests = db.Column(db.String(80), unique=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "friends": self.friends,
            "pending_friend_requests": self.pending_friend_requests,
            "sent_friend_requests": self.sent_friend_requests,
            "gym": self.gym,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Posting(db.Model):
    __tablename__ = "posting"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    def __repr__(self):
        return f'<Posting {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user
            
            # do not serialize the password, its a security breach
        }

class Gym(db.Model):
    __tablename__ = "gym"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)
   

    def __repr__(self):
        return f'<Posting {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "user": self.user
            
            # do not serialize the password, its a security breach
        }