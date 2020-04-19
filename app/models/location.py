from sqlalchemy.sql import func

from app import db
from app.models.model_json import ModelJson


class Location(db.Model, ModelJson):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.String(15), nullable=True)
    longitude = db.Column(db.String(15), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    deleted = db.Column(db.Boolean, default=False)

    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())

