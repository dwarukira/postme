from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask import url_for

from . import db



class User(db.Model):
    __tablename__ ='users'

    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128) , unique=True)

    photo = db.Column(db.String(128))

    password_hash = db.Column(db.String(128))



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash , password)

    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        return {
                'username':self.username,
                "email":self.email,
                "photo":self.photo}
def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    if user and user.check_password(password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id == payload['identity']).scalar()


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(128), unique=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def to_dict(self):
        return {
                "id":self.id,
                "title":self.title,
                "content":self.content,
                "author":url_for('api.user', id=self.user_id,_external=True),
                "timestamp":self.timestamp}

    def save(self):
        db.session.add(self)
        db.session.commit()

    
