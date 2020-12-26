from flask_sqlalchemy import SQLAlchemy
from db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(64))
    def __repr__(self):
        return '<User %r>' % self.username