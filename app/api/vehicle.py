from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy_utils.types.json import json

from app import db
from app.models import Vehicle, AdminUser
from app.models.location import Location
from app.utils.database import Database
from app.utils.utls import build_response
from . import api

database = Database(db.session, Vehicle)


@api.route('/vehicle', methods=["POST"])
@jwt_required
def add_vehicle():
    data = request.json
    return build_response(database.save, **data)


@api.route('/vehicle/<int:vehicle_id>', methods=["DELETE"])
@jwt_required
def delete_vehicle(vehicle_id):
    """
    Method to delete vehicle with id
    :param vehicle_id:
    :return:
    """
    return build_response(database.delete, id=vehicle_id)


@api.route('/vehicle/<int:vehicle_id>', methods=["PUT"])
@jwt_required
def edit_vehicle(vehicle_id):
    data = request.json
    return build_response(database.update, data=data, **{
        "id": vehicle_id
    })


@api.route('/vehicle/<int:vehicle_id>', methods=["GET"])
@jwt_required
def get_vehicle(vehicle_id):
    return build_response(database.get, id=vehicle_id)


@api.route('/vehicle/<int:vehicle_id>/last-location', methods=["GET"])
@jwt_required
def last_location(vehicle_id):
    vehicle = database.get(id=vehicle_id)
    last_location = vehicle.locations.order_by(Location.time_created.desc()).first()
    if not last_location:
        return jsonify({"error": True, "message": "location not found"}), 404
    return last_location.to_json()

@api.route('/get_my_vehicles', methods=["GET"])
@jwt_required
def get_vehicles():
    identity = get_jwt_identity()
    user_id = identity.get("id")
    database = Database(db.session, AdminUser)
    user = database.get(id=user_id)
    if not user:
        return jsonify({"error": True, "message": "User not found"}), 404
    vehicles = user.vehicles
    return {
        "count": len(vehicles),
        "vehicles": [vehicle.to_json() for vehicle in vehicles]
    }
