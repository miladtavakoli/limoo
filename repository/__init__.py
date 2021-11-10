from os import getenv
import pymssql

from model.user import User

server = "localhost:1433"
user = "SA"
password = "MLDn00b2357"


class DatabaseConnection:
    def __init__(self):
        self.con = pymssql.connect(server, user, password, "parsdata")
        self.cursor = self.con.cursor(as_dict=True)

    def __enter__(self):
        return self.cursor

    def __exit__(self, type, value, traceback):
        self.con.close()
        self.cursor.close()


# db = DatabaseConnection()
#
# db.cursor.callproc('FindUser', ('00989373875028',))
# for row in db.cursor:
#     u = User.from_dict(row)
#     print(u)
#

