import base64
import hmac
import hashlib
import json
from datetime import datetime, timedelta

from utils.exceptions import JwtFormatException, JwtAuthorizationException


class CustomJwt:
    def __init__(self):
        self.header = {}
        self.payload = {}
        self.token = ""

    @staticmethod
    def _convert_dict_to_b64(input_data: dict) -> str:
        input_data = json.dumps(input_data).encode("ascii")
        return base64.b64encode(input_data).decode("ascii")

    @staticmethod
    def _convert_b64_to_dict(b64_string: str) -> dict:
        b64_string = b64_string.encode("ascii")
        input_payload = base64.b64decode(b64_string).decode("ascii")
        input_payload = input_payload.replace("'", '"')
        return json.loads(input_payload)

    @staticmethod
    def _calculate_expire_time(expired_time: int) -> int:
        expired_at = datetime.now() + timedelta(seconds=expired_time)
        return int(expired_at.timestamp())

    @staticmethod
    def _get_token(bearer_token: str) -> str:
        jwt_token = bearer_token.split(" ")
        if len(jwt_token) < 2:
            raise JwtFormatException("JWT has not valid format")
        return jwt_token[1]

    def _build_token(self) -> str:
        # TODO:
        #   read secret key from env
        secret_key = "SECRET_KEY"
        b_payload = self._convert_dict_to_b64(self.payload).encode("ascii")
        return hmac.new(secret_key.encode("ascii"), b_payload, hashlib.sha256).hexdigest()

    def _set_header(self):
        self.header = {
            "alg": "hs256",
            "typ": "jwt",
        }
        return

    def _set_payload(self, user_id: int, expired_time: int, refresh_token: bool) -> None:
        self.payload = {
            "user_id": user_id,
            "expired_at": self._calculate_expire_time(expired_time),

        }
        if refresh_token:
            self.payload["refresh_token"] = True
        return

    def _set_token(self) -> None:
        self.token = self._build_token()
        return

    def _is_valid_token(self) -> bool:
        token = self._build_token()
        return self.token == token

    def _is_token_expired(self) -> bool:
        return self.payload.get("expired_at") < datetime.now().timestamp()

    def create_jwt(self, user_id: int, expired_time: int, refresh_token=False) -> str:
        self._set_header()
        self._set_payload(user_id, expired_time, refresh_token=refresh_token)
        self._set_token()
        return f"{self._convert_dict_to_b64(self.header)}." \
               f"{self._convert_dict_to_b64(self.payload)}." \
               f"{self.token}"

    def verify_jwt(self, bearer_token, refresh_token=False):
        jwt_token = self._get_token(bearer_token)
        jwt_token = jwt_token.split(".")
        if len(jwt_token) != 3:
            raise JwtFormatException("Jwt has not valid format.")
        b64_header, b64_payload, self.token = jwt_token
        self.payload = self._convert_b64_to_dict(b64_payload)
        if not self._is_valid_token():
            raise JwtAuthorizationException("Jwt is not valid.")
        if self._is_token_expired():
            raise JwtAuthorizationException("Jwt expired.")
        return True


def create_access_token(user_id: int, expired_time: int = 3000) -> str:
    custom_jwt = CustomJwt()
    return custom_jwt.create_jwt(user_id, expired_time=expired_time)


def create_refresh_token(user_id: int, expired_time: int = 3000) -> str:
    custom_jwt = CustomJwt()
    return custom_jwt.create_jwt(user_id, expired_time, refresh_token=True)
