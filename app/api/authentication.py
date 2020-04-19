from flask import request, jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.orm.exc import NoResultFound

from app import db
from app.models import AdminUser
from app.utils.database import Database
from . import api

database = Database(db.session, AdminUser)


@api.route('/auth', methods=["POST"])
def get_jwt():
    """
    Method to validate user and get JWT
    """
    data = request.json
    username = data.get("username")
    password = data.get("password")
    try:
        user = database.get(username=username)  # type: AdminUser
    except NoResultFound:
        return jsonify({"error": "not valid user"}), 401
    if not user.validate_password(password):
        return jsonify({"error": "not valid user"}), 401

    jwt = create_access_token(identity=user.to_json())
    return jsonify({"jwt": jwt}), 200
