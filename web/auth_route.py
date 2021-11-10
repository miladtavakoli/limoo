from flask import Blueprint, request

from repository.user import UserRepository
from use_case.auth_use_case import UserLoginUseCase
from utils.response_helper import successful_response

auth = Blueprint("auth", __name__, url_prefix="/auth/")


@auth.route("login/", methods=["GET"])
def login():
    data = request.get_json(silent=True)
    use_case = UserLoginUseCase(UserRepository())
    result = use_case.execute(data)
    return successful_response(result)
