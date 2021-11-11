from flask import Blueprint, request, jsonify

from repository.user import UserRepository
from use_case.auth_use_case import UserLoginUseCase, CreateProfile
from utils.authorization import authorization, get_current_user
from utils.exceptions import JwtException, ValidationException, JwtAuthorizationException, CustomException, \
    LoginUnsuccessfulException
from utils.response_helper import successful_response, error_response

auth = Blueprint("auth", __name__, url_prefix="/auth/")


@auth.route("login/", methods=["POST"])
def login():
    try:
        data = request.get_json(silent=True)
        use_case = UserLoginUseCase(UserRepository())
        result = use_case.execute(data)
    except ValidationException as e:
        return error_response(data=str(e), status_code=400)
    return successful_response(result)


@auth.route("create-profile/", methods=["POST"])
@authorization
def create_profile():
    try:
        data = request.get_json(silent=True)
        user = get_current_user()
        use_case = CreateProfile(UserRepository())
        result = use_case.execute(data, user)
    except JwtException as e:
        return error_response(data=str(e), status_code=401)
    return successful_response(result)

