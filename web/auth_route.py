from flask import Blueprint

from utils.response_helper import successful_response

auth = Blueprint("auth", __name__, url_prefix="/auth/")


@auth.route("ping/", methods=["GET"])
def ping():
    result = {"ping": "pong"}
    return successful_response(result)
