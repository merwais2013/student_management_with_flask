from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired


class CourseForm(FlaskForm):
    course_name = StringField('Course name', validators=[DataRequired()])
    description = TextAreaField('Teacher description', validators=[DataRequired()])
    submit = SubmitField('Add Course')