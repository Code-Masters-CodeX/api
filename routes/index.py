from flask import Blueprint, jsonify

api_blueprint = Blueprint('api', __name__);

@api_blueprint.route('/')
def index():
    data = {
        "message": "api end point"
    }

    return jsonify(data);