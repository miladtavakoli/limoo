from model.user import User
from repository import DatabaseConnection


class UserRepository(DatabaseConnection):
    def _create_find_users_procedure(self):
        self.cursor.execute("""
                            CREATE PROCEDURE FindUser 
                            @msisdn varchar(15)
                            AS BEGIN
                            SELECT * FROM parsdata.limoo.users u WHERE u.msisdn  = @msisdn;
                            END
                            """)
        return

    def find_user(self, phone_number):
        self._create_find_users_procedure()
        self.cursor.callproc('FindUser', (phone_number,))
        return [User.from_dict(r) for r in self.cursor]


