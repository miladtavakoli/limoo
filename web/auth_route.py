from flask import Blueprint, request, jsonify, g

from repository.user import UserRepository
from use_case.auth_use_case import UserLoginUseCase, UpdateProfile, GetCurrentUserProfile, RefreshAccessToken
from utils.authorization import authorization, get_current_user, authorization_refresh_token
from utils.custom_jwt import create_access_token
from utils.exceptions import JwtException, ValidationException, CustomException
from utils.response_helper import successful_response, error_response

auth = Blueprint("auth", __name__, url_prefix="/auth/")


@auth.errorhandler(CustomException)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@auth.route("login/", methods=["POST"])
def login():
    try:
        data = request.get_json(silent=True)
        use_case = UserLoginUseCase(UserRepository())
        result = use_case.execute(data)
    except ValidationException as e:
        return error_response(data=str(e), status_code=400)
    return successful_response(result)


@auth.route("refresh-token/", methods=["GET"])
@authorization_refresh_token
def refresh_token():
    use_case = RefreshAccessToken()
    result = use_case.execute(g.user_id)
    return successful_response(result)


@auth.route("update-profile/", methods=["POST"])
@authorization
def create_profile():
    try:
        data = request.get_json(silent=True)
        user = get_current_user()
        use_case = UpdateProfile(UserRepository())
        result = use_case.execute(data, user)
    except JwtException as e:
        return error_response(data=str(e), status_code=401)
    return successful_response(result)


@auth.route("me/", methods=["GET"])
@authorization
def get_current_user_profile():
    try:
        user = get_current_user()
        use_case = GetCurrentUserProfile()
        result = use_case.execute(user)
    except JwtException as e:
        return error_response(data=str(e), status_code=401)
    return successful_response(result)
