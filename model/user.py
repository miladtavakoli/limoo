class User:
    def __init__(self, id, msisdn, created_at, last_login):
        self.id = id
        self.msisdn = msisdn
        self.created_at = created_at
        self.last_login = last_login

    @classmethod
    def from_dict(cls, input_dict):
        return cls(**input_dict)

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "msisdn": self.msisdn,
            "created_at": self.created_at,
            "last_login": self.last_login,
        }

    def __repr__(self):
        return f"<User id: {self.id}>"
