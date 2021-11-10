from flask import jsonify, request


class CustomException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        response = {'message': self.message}
        return response


class JwtException(CustomException):
    def __init__(self, message="Authorization Exception error."):
        CustomException.__init__(self, message, status_code=401)


class JwtFormatException(JwtException):
    pass


class JwtAuthorizationException(JwtException):
    pass


class NotFoundException(Exception):
    pass


class ValidationException(CustomException):
    def __init__(self, message="Check you`r inputs.Try again."):
        CustomException.__init__(self, message, status_code=400)
