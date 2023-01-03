# Users model
from student_project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin, current_user
from student_project import admin
from flask_admin.contrib.sqla import ModelView


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Integer, nullable=False, default=0)
    profile_pic = db.Column(db.String(200), nullable=False, default='default.jpg')
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(50), nullable=True)
    password_hash = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=True)
    teachers = db.relationship('Teacher', backref='author', lazy=True)
    courses = db.relationship('Course', backref='author1', lazy=True)

    def __init__(self, full_name, email, phone_number, password):
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Your Full name is: {self.full_name}"


class Teacher(db.Model):
    __tablename__ = 'teachers'
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    teacher_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    teach_profile = db.Column(db.String(200), nullable=False, default='default.jpg')
    courses = db.relationship('Course', backref='author2', lazy=True)

    def __init__(self, teacher_name, email, description, teach_profile, user_id):
        self.teacher_name = teacher_name
        self.email = email
        self.description = description
        self.teach_profile = teach_profile
        self.user_id = user_id

    def __repr__(self):
        return f"Your Full name is: {self.teacher_name}"


class Course(db.Model):
    __tablename__ = 'courses'
    users = db.relationship(User)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, course_name, description, user_id, teacher_id):
        self.course_name = course_name
        self.description = description
        self.user_id = user_id
        self.teacher_id = teacher_id

    def __repr__(self):
        return f"Course is: {self.course_name}"


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Teacher, db.session))
admin.add_view(ModelView(Course, db.session))
