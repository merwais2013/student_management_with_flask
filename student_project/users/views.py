# user/ views

from flask import Blueprint, render_template, flash, redirect, url_for, request
from student_project import db
from student_project.models import User
from student_project.users.forms import LoginForm, RegisterForm, AccountForm
from flask_login import login_required, login_user, logout_user, current_user
from student_project.users.picture_handler import add_profile_pic, admin_only

user_blueprint = Blueprint('users', __name__)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully😍")
    return redirect(url_for('core.index'))


@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(full_name=form.full_name.data, email=form.email.data, phone_number=form.phone_number.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have registered successfully, Now you can log In.🥰")
        return redirect(url_for('users.login'))
    return render_template("register.html", form=form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email")).first()
        if user.check_password(request.form.get("password")) and user is not None:
            login_user(user)
            flash("Logged In successfully😍")
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
        print(request.form.get("email"))
        print("hello")
    return render_template("login.html", form=form)


@user_blueprint.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            pic = add_profile_pic(form.picture.data)
            current_user.profile_pic = pic
        current_user.full_name = form.full_name.data
        current_user.email = form.email.data
        current_user.phone_number = form.phone_number.data
        db.session.commit()
        flash("Your account has been updated!😇")
    elif request.method == 'GET':
        form.full_name.data = current_user.full_name
        form.email.data = current_user.email
        form.phone_number.data = current_user.phone_number
    profile_image = url_for('static', filename='images/' + current_user.profile_pic)
    return render_template("account.html", form=form, profile_image=profile_image, full_name=current_user.full_name)


@user_blueprint.route("/admin-page")
@admin_only
def admin_page():
    return render_template("admin.html")

@user_blueprint.route("/student-course")
def student_course():

    pass