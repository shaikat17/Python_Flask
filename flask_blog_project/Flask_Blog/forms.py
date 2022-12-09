from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, PasswordField, StringField, validators
from Flask_Blog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(
        'Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField(
        'Email Address', [validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired()
    ])
    confirm_password = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise validators.ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise validators.ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(
        'Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired()])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Login')
