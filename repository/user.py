import pymssql

from model.user import User
from utils.exceptions import NotFoundException

server = "localhost:1433"
user = "SA"
password = "MLDn00b2357"


class UserRepository:
    @staticmethod
    def find_one_user_by_msisdn(msisdn: str):
        conn = pymssql.connect(server, user, password, "parsdata")
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('FindUserByMsisdn', (msisdn,))
        r = [User.from_dict(r) for r in cursor]
        if len(r) < 1:
            raise NotFoundException("User not found.")
        conn.close()
        return r[0]

    @staticmethod
    def find_one_user_by_id(id: str):
        conn = pymssql.connect(server, user, password, "parsdata")
        cursor = conn.cursor(as_dict=True)
        cursor.callproc('FindUserId', (id,))
        r = [User.from_dict(r) for r in cursor]
        if len(r) < 1:
            raise NotFoundException("User not found.")
        conn.close()
        return r[0]
