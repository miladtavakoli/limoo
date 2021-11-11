import pymssql

from model.user import User
from utils.exceptions import NotFoundException
import config


class UserRepository:
    @staticmethod
    def find_one_user_by_msisdn(msisdn: str):
        conn = pymssql.connect(config.SQL_URL, config.SQL_USERNAME, config.SQL_PASSWORD, config.SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('limoo.find_user_by_msisdn', (msisdn,))
        r = [User.from_dict(r) for r in cursor]
        if len(r) < 1:
            raise NotFoundException("User not found.")
        conn.close()
        return r[0]

    @staticmethod
    def find_one_user_by_id(id: int):
        conn = pymssql.connect(config.SQL_URL, config.SQL_USERNAME, config.SQL_PASSWORD, config.SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('limoo.find_user_by_id', (id,))
        r = [User.from_dict(r) for r in cursor]
        if len(r) < 1:
            raise NotFoundException("User not found.")
        conn.close()
        return r[0]

    @staticmethod
    def update_first_name_last_name_by_id(id: int, first_name: str = None, last_name: str = None):
        conn = pymssql.connect(config.SQL_URL, config.SQL_USERNAME, config.SQL_PASSWORD, config.SQL_DATABASE)
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('limoo.update_first_name_last_name_by_id', (id, first_name, last_name))
        conn.commit()
        conn.close()
        return
