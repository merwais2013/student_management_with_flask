# Student Project file

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
basedir = os.path.abspath(os.path.dirname(__file__))
from flask_admin import Admin

login_manager = LoginManager()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'itismysecretkey'
app.app_context().push()
db = SQLAlchemy(app)
admin = Admin(app)
migrate = Migrate(app, db)
login_manager.init_app(app)
login_manager.login_view = 'users.login'
from student_project.core.views import core_blueprint
from student_project.users.views import user_blueprint
from student_project.teachers.views import teacher_blueprint
from student_project.courses.views import course_blueprint

app.register_blueprint(core_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(teacher_blueprint)
app.register_blueprint(course_blueprint)