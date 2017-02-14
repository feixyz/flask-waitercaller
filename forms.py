from flask_wtf import FlaskForm as Form
from wtforms import PasswordField, SubmitField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class RegistrationForm(Form):
    email = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('password', validators=[validators.DataRequired(), validators.Length(min=6, message='Please choose a password of at least 6 characters.')])
    password2 = PasswordField('password2', validators=[validators.DataRequired(), validators.EqualTo('password', message='Passwords mush match.')])
    submit = SubmitField('submit', validators=[validators.DataRequired()])

class LoginForm(Form):
    loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    loginpassword = PasswordField('password', validators=[validators.DataRequired(message='Password field is required.')])
    submit = SubmitField('submit', validators=[validators.DataRequired()])

class CreateTableForm(Form):
    tablenumber = TextField('tablenumber', validators=[validators.DataRequired()])
    submit = SubmitField('createtablesubmit', validators=[validators.DataRequired()])