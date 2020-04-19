from flask_login import UserMixin
from passlib.hash import bcrypt
from sqlalchemy.sql import func

from app import db
from app.models.model_json import ModelJson


class AdminUser(UserMixin, db.Model, ModelJson):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.UnicodeText, nullable=False)
    email = db.Column(db.String, nullable=False, unique=False)
    username = db.Column(db.String, nullable=True, unique=True)
    active = db.Column(db.Boolean, default=False)
    password = db.Column(db.String, nullable=True)
    deleted = db.Column(db.Boolean, default=False)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), server_default=func.now())
    vehicles = db.relationship('Vehicle',
                               cascade="all, delete-orphan",
                               single_parent=True)

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)

    def set_password(self, password):
        self.password = bcrypt.hash(password)
        return self.password

    def __repr__(self):
        return "<{}, {}>".format(self.__class__.email, self.id)
