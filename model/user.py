class User:
    def __init__(self, id, msisdn, password, avatar):
        self.id = id
        self.msisdn = msisdn
        self.password = password
        self.avatar = avatar

    @classmethod
    def from_dict(cls, input_dict):
        return cls(**input_dict)

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "msisdn": self.msisdn,
            "password": self.password,
            "avatar": self.avatar,
        }

    def __repr__(self):
        return f"<User id: {self.id}>"
