from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from datetime import datetime
from user import User

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    "postgresql://postgres:n0password1@localhost"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #enable automatic commits of database changes at the end of each request
db = SQLAlchemy(app)


#user_john = User(username='john', password='nopassword', email='someone+testing@gmail.com')
#db.session.add(user_john)
#db.session.commit()