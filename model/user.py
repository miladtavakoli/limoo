class User:
    def __init__(self, id=None, msisdn=None, created_at=None, first_name=None, last_name=None, avatar=None):
        self.id = id
        self.msisdn = msisdn
        self.created_at = created_at
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

    @classmethod
    def from_dict(cls, input_dict):
        return cls(**input_dict)

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "msisdn": self.msisdn,
            "created_at": self.created_at,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
        }

    def __repr__(self):
        return f"<User id: {self.id}>"
