from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import flask_login

auth = flask_login.LoginManager()
def create_app():
    app = Flask(__name__)
    app.secret_key = '$:c{%;cW=927DHTN'
    auth.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:n0password1@localhost"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # enable automatic commits of database changes at the end of each request
    return app

app = create_app()