# __init__.py
from flask import Flask
from flask_login import LoginManager
from mongoengine import connect
from .models import User, JobPost, Application, Course, UserCourseProgress

app = Flask(__name__)
app.secret_key = 'supersecretkey'
login_manager = LoginManager(app)
login_manager.init_app(app)

# Connecting to MongoDB Atlas
connect(db="jobhub_db", host="mongodb+srv://itumeleng:Itumeleng1.@cluster0.3klnl.mongodb.net/")

@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

from . import routes  # Import routes after initializing app and models

