from flask import Blueprint, jsonify, make_response

auth = Blueprint("auth", __name__, url_prefix="/auth/")


@auth.route("ping/", methods=["GET"])
def ping():
    return make_response(jsonify({"ping": "pong"}))
