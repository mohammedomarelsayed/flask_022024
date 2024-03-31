from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import data_required, length, Email, Regexp, EqualTo

class RegistrationForm (FlaskForm):
    fname = StringField('First Name', validators=[data_required(), length(min = 2, max=25)])
    lname = StringField('Last Name', validators=[data_required(), length(min = 2, max=25)])
    username = StringField('User Name', validators=[data_required(), length(min = 2, max=25)])
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required(),
        Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$")])
    confirm_password = PasswordField('Confirm_password', validators=[data_required(), EqualTo(password)])

    submit = SubmitField('Sign Up')

class LoginForm (FlaskForm):
    
    email = StringField('Email', validators=[data_required(), Email()])
    password = PasswordField('Password', validators=[data_required(),
        Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$")])
    remember = BooleanField ('Remember Me')