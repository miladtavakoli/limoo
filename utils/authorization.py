from functools import wraps

from flask import request, g

from repository.user import UserRepository
from utils.custom_jwt import CustomJwt
from utils.exceptions import JwtAuthorizationException


def authorization(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if "Authorization" not in request.headers:
            raise JwtAuthorizationException("Authorization was not send")
        bearer_token = request.headers.get("Authorization", " ")
        c = CustomJwt()
        c.verify_jwt(bearer_token)
        g.user_id = c.payload.get("user_id")
        return f(*args, **kwargs)

    return inner


def authorization_refresh_token(f):
    @wraps(f)
    def inner(*args, **kwargs):
        if "Authorization" not in request.headers:
            raise JwtAuthorizationException("Authorization was not send")
        bearer_token = request.headers.get("Authorization", " ")
        c = CustomJwt()
        c.verify_jwt(bearer_token, refresh_token=True)
        g.user_id = c.payload.get("user_id")
        return f(*args, **kwargs)
    return inner


def get_current_user():
    u_r = UserRepository()
    user = u_r.find_one_user_by_id(g.user_id)
    return user
