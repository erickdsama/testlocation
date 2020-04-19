from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

method_response = {
    "POST": 201,
    "PUT": 202,
    "GET": 200,
    "DELETE": 202
}


def build_response(method, **kwargs):
    try:
        obj = method.__call__(**kwargs)
    except NoResultFound:
        return jsonify({
            "error": True,
            "message": "Not Found"
        }), 404
    except IntegrityError as e:
        return jsonify({
            "error": True,
            "message": str(e)
        }), 409
    except Exception as e:
        return jsonify({
            "error": True,
            "message": str(e)
        }), 500

    return jsonify(obj.to_json()), method_response.get(request.method, 200)
