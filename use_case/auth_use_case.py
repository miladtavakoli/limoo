from model.user import User
from utils.custom_jwt import create_access_token, create_refresh_token
from utils.exceptions import ValidationException, NotFoundException, LoginUnsuccessfulException


class UserLoginUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def _validate_msisdn(msisdn: str) -> str:
        if msisdn is None:
            raise ValidationException("Please enter your phone number.")
        if not isinstance(msisdn, str) or len(msisdn) < 10:
            raise ValidationException("Please valid phone number.")
        return msisdn

    def _validate_input(self, input_dict: dict) -> str:
        if not isinstance(input_dict, dict):
            raise ValidationException("Json was not send.")
        msisdn = self._validate_msisdn(input_dict.get("msisdn"))
        return msisdn

    def execute(self, input_dict: dict) -> dict:
        msisdn = self._validate_input(input_dict)
        try:
            user = self.user_repo.find_one_user_by_msisdn(msisdn)
        except NotFoundException as e:
            raise LoginUnsuccessfulException
        result = {
            "access_token": create_access_token(user.id),
            "refresh_token": create_refresh_token(user.id),
        }
        return result


class CreateProfile:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def _validate_first_name(first_name: str) -> str:
        if len(first_name) < 2:
            raise ValidationException("Enter valid first name.")
        return first_name

    @staticmethod
    def _validate_last_name(last_name: str) -> str:
        if len(last_name) < 2:
            raise ValidationException("Enter valid last name.")
        return last_name

    def _validate_input(self, input_dict: dict) -> (str, str):
        if not isinstance(input_dict, dict):
            raise ValidationException("Json was not send.")
        first_name = self._validate_first_name(input_dict.get("first_name", ""))
        last_name = self._validate_last_name(input_dict.get("last_name", ""))
        return first_name, last_name

    def execute(self, input_dict: dict, user: User) -> dict:
        user.first_name, user.last_name = self._validate_input(input_dict)
        self.user_repo.update_first_name_last_name_by_id(user.id, user.first_name, user.last_name)
        result = {"profile": "created"}
        return result


class GetCurrentUserProfile:
    @staticmethod
    def execute(user: User) -> dict:
        return user.to_dict


class RefreshAccessToken:
    @staticmethod
    def execute(user_id: int) -> dict:
        return {"access_token": create_access_token(user_id)}
