class Profile:
    def __init__(self, id, first_name, last_name, avatar, user_id):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar
        self.user_id = user_id

    @classmethod
    def from_dict(cls, input_dict):
        return cls(**input_dict)

    @property
    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "avatar": self.avatar,
            "user_id": self.user_id,
        }
