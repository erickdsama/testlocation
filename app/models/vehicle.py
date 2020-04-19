from sqlalchemy.sql import func

from app import db
from app.models.model_json import ModelJson


class Vehicle(db.Model, ModelJson):
    __tablename__ = "vehicle"

    id = db.Column(db.Integer, primary_key=True)
    vin = db.Column(db.String(18), nullable=True)
    plate = db.Column(db.String(10), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    deleted = db.Column(db.Boolean, default=False)

    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), server_default=func.now())

    locations = db.relationship('Location',
                                cascade="all, delete-orphan",
                                lazy="dynamic",
                                single_parent=True)
