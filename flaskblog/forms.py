from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(2, 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('ConfirmPassword', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Signup')


    def validate_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError('User already exits!')


    def validate_email(self, email):
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError('Email already exits!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')