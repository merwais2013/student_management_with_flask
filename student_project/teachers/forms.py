from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileAllowed, FileField


class TeacherForm(FlaskForm):
    teacher_name = StringField('Teacher name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    description = TextAreaField('Teacher description', validators=[DataRequired()])
    profile = FileField('Profile Picture', validators=[DataRequired(), FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Add Teacher')
