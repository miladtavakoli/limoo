import pymssql

from model.user import User
from utils.exceptions import NotFoundException

server = "localhost:1433"
user = "SA"
password = "MLDn00b2357"


class UserRepository:
    @staticmethod
    def find_one_user(phone_number: str):
        conn = pymssql.connect(server, user, password, "parsdata")
        cursor = conn.cursor(as_dict=True)
        cursor.execute("""
                    CREATE PROCEDURE FindUser @msisdn varchar(15)
                    AS BEGIN
                    SELECT * FROM parsdata.limoo.users u WHERE u.msisdn  = @msisdn;
                    END
                    """)
        cursor.callproc('FindUser', (phone_number,))
        r = [User.from_dict(r) for r in cursor]
        if len(r) < 1:
            raise NotFoundException("User not found.")
        return r[0]