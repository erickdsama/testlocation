from flask import request
from flask_jwt_extended import jwt_required

from app import db
from app.models.user import AdminUser
from app.utils.database import Database
from app.utils.utls import build_response
from . import api

database = Database(db.session, AdminUser)


@api.route('/user', methods=["POST"])
def add_user():
    data = request.json
    return build_response(database.save_user, **data)


@api.route('/user/<int:user_id>', methods=["DELETE"])
@jwt_required
def delete_user(user_id):
    """
    Method to delete user with id
    :param user_id:
    :return:
    """
    return build_response(database.delete, id=user_id)


@api.route('/user/<int:user_id>', methods=["PUT"])
@jwt_required
def edit_user(user_id):
    data = request.json
    return build_response(database.update, data=data, **{
        "id": user_id
    })


@api.route('/user/<int:user_id>', methods=["GET"])
@jwt_required
def get_user(user_id):
    return build_response(database.get, id=user_id)


