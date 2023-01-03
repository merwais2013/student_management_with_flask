# core views file
from flask import Blueprint, render_template
from student_project.models import User
core_blueprint = Blueprint('core', __name__)

# More to come


@core_blueprint.route("/")
def index():
    students = User.query.all()
    print(students)
    return render_template("index.html", students=students)


@core_blueprint.route("/info")
def info():
    return render_template("info.html")