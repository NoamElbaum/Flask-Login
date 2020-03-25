from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, StringField


class LogInForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit = SubmitField('Log in')
