# My goal for this break is to produce a small SPA that allows a user:
# register their email address, username and password to a database (postgres backed)
# and allows the user to communicate via  small messenger application
from flask import Flask, request, url_for, redirect
import flask_login

app = Flask(__name__)
app.secret_key = '$:c{%;cW=927DHTN'
auth = flask_login.LoginManager()
auth.init_app(app)

users = {'bob': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass

@auth.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@auth.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

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
    if request.form['password'] == users[email]['password']:
        user = User()
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

    # import sqlite3
    #
    # conn = sqlite3.connect('photoshare.db')
    #
    # c = conn.cursor()
    #
    # # Create table
    # c.execute('''CREATE TABLE users
    #              (id int, trans text, symbol text, qty real, price real)''')
    #
    # # Insert a row of data
    # c.execute("INSERT INTO users VALUES ('','BUY','RHAT',100,35.14)")
    #
    # # Save (commit) the changes
    # conn.commit()
    #
    # # We can also close the connection if we are done with it.
    # # Just be sure any changes have been committed or they will be lost.
    # conn.close()
