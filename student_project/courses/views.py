from flask import Blueprint, render_template, redirect, url_for
from student_project.courses.forms import CourseForm
from student_project.models import Course
from flask_login import current_user, login_required
from student_project import db
from student_project.users.picture_handler import add_profile_pic

course_blueprint = Blueprint('courses', __name__)


@course_blueprint.route('/view-course')
def view_course():
    courses = Course.query.all()
    for course in courses:
        print(course.course_name)
    return render_template("course.html", courses=courses)


@course_blueprint.route("/add-course", methods=['GET', 'POST'])
@login_required
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        new_course = Course(course_name=form.course_name.data,
                            description=form.description.data,
                            user_id=current_user.id, teacher_id=current_user.id)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('courses.view_course'))
    return render_template('add_course.html', form=form)
