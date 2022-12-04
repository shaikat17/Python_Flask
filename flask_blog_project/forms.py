from wtforms import Form, BooleanField, SubmitField, PasswordField, StringField, validators


class RegistrationForm(Form):
    username = StringField(
        'Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField(
        'Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm_password = PasswordField('Repeat Password', [
        validators.DataRequired()])
    submit = SubmitField('Sign Up')


class LoginForm(Form):
    email = StringField(
        'Email Address', [validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('New Password', [
        validators.DataRequired()])
    remember = BooleanField('Remember Password', [
        validators.DataRequired()])
    submit = SubmitField('Login')
