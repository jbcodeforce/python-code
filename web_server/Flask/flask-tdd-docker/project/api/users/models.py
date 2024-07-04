# project/api/models.py

from sqlalchemy.sql import func
from flask_admin.contrib.sqla import ModelView 
from project import db
import os


class User(db.Model):
    """
    Define users table model and a User bean
    parameter: a SQLAlchemy database
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username = '', email = ''):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "active": self.active,
        }

if os.getenv("FLASK_ENV") == "development":
    from project import admin
    from project.api.users.admin import UsersAdminView  
    admin.add_view(UsersAdminView(User, db.session))

