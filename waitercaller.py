from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_required, login_user, logout_user
from user import User
import config
if config.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    pass

DB = DBHelper()

app = Flask(__name__)
app.secret_key = 'a4e13nbyQdfMo1SGxchbGM8zLj+fCDR9lg07wxFiyVagq1cwdlUlYW3uXSGRXPof'

login_manager = LoginManager(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user_password = DB.get_user(email)

    if user_password and user_password == password:
        user = User(email)
        login_user(user)
        return redirect(url_for('account'))
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return "You are logged in"

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

if __name__ == '__main__':
    app.run(port=5000, debug=True)