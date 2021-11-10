from utils.custom_jwt import create_access_token, create_refresh_token


class UserLoginUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    @staticmethod
    def _validate_msisdn(msisdn: str) -> str:
        if msisdn is None:
            raise Exception("Please enter your phone number.")
        if not isinstance(msisdn, str) or len(msisdn) < 10:
            raise Exception("Please valid phone number.")
        return msisdn

    def _validate_input(self, input_dict: dict) -> str:
        msisdn = self._validate_msisdn(input_dict.get("msisdn"))
        return msisdn

    def execute(self, input_dict):
        msisdn = self._validate_input(input_dict)
        print(msisdn)
        user = self.user_repo.find_one_user(msisdn)
        result = {
            "access_token": create_access_token(user.id, expired_time=300),
            "refresh_token": create_refresh_token(user.id, expired_time=3000),
        }
        return result
