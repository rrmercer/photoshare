from flask import Flask, request, url_for, redirect
import flask_login

from model.user import User
from app import app, auth


class AuthUser(flask_login.UserMixin):
    pass

@auth.user_loader
def user_loader(email):
    user_returned = User.query.filter_by(username=email).all()
    if not user_returned:
        return

    user = AuthUser()
    user.id = email
    return user


@auth.request_loader
def request_loader(request):
    email = request.form.get('email')
    user_returned = User.query.filter_by(username=email).all()
    if not user_returned:
        return

    user = AuthUser()
    user.id = email

    user.is_authenticated = len(user_returned) > 0 and request.form['password'] == user_returned[0].password
    return user

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='/login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    user_returned = User.query.filter_by(username=email).all()
    if len(user_returned) > 0 and request.form['password'] == user_returned[0].password:
        user = AuthUser()
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@auth.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

if __name__ == '__main__':
    app.run(debug=True)

