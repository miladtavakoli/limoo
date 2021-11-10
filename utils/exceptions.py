class JwtException(Exception):
    pass


class JwtFormatException(JwtException):
    pass


class JwtAuthorizationException(JwtException):
    pass


class NotFoundException(Exception):
    pass
