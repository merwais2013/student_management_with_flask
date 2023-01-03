from flask import Blueprint, render_template, redirect, url_for
from student_project.models import Teacher
from student_project.teachers.forms import TeacherForm
from student_project.users.picture_handler import add_profile_pic
from flask_login import current_user, login_required
from student_project import db
teacher_blueprint = Blueprint('teachers', __name__)


@teacher_blueprint.route("/view-teacher")
@login_required
def view_teacher():
    teachers = Teacher.query.all()
    return render_template("teacher.html", teachers=teachers)


@teacher_blueprint.route("/add-teacher", methods=['GET', 'POST'])
@login_required
def add_teacher():
    form = TeacherForm()
    if form.validate_on_submit():
        if form.profile.data:
            pic = add_profile_pic(form.profile.data)

        new_teacher = Teacher(teacher_name=form.teacher_name.data, email=form.email.data,
                              description=form.description.data, teach_profile=pic,
                              user_id=current_user.id)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('teachers.view_teacher'))
    return render_template("add_teacher.html", form=form)