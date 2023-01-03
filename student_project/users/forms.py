# User forms

from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, FileField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from student_project.models import User
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    full_name = StringField('Enter your full name', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    password = PasswordField('Enter your password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegisterForm(FlaskForm):
    full_name = StringField('Enter your full name', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    phone_number = StringField('Enter your number', validators=[DataRequired()])
    password = PasswordField('Enter your password', validators=[DataRequired(), EqualTo('confirm_pass')])
    confirm_pass = PasswordField('Confirm your password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been already registered😮.')


class AccountForm(FlaskForm):
    full_name = StringField('Your full name', validators=[DataRequired()])
    email = StringField('Your email', validators=[DataRequired(), Email()])
    phone_number = StringField('Your number', validators=[DataRequired()])
    picture = FileField('Update your profile', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Update account!')
