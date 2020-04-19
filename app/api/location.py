from flask import request
from flask_jwt_extended import jwt_required

from app import db
from app.models.location import Location
from app.utils.database import Database
from app.utils.utls import build_response
from . import api

database = Database(db.session, Location)


@api.route('/location', methods=["POST"])
@jwt_required
def add_location():
    data = request.json
    return build_response(database.save, **data)


@api.route('/location/<int:location_id>', methods=["DELETE"])
@jwt_required
def delete_location(location_id):
    """
    Method to delete location with id
    :param location_id:
    :return:
    """
    return build_response(database.delete, id=location_id)


@api.route('/location/<int:location_id>', methods=["PUT"])
@jwt_required
def edit_location(location_id):
    data = request.json
    return build_response(database.update, data=data, **{
        "id": location_id
    })


@api.route('/location/<int:location_id>', methods=["GET"])
@jwt_required
def get_location(location_id):
    return build_response(database.get, id=location_id)


