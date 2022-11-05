from exceptions import ValidationError


class Player:

    def __init__(self, username, fullname):
        self.username = username
        self.fullname = fullname

    def validate(self):
        if not (self.username or self.fullname):
            raise ValidationError(f"{self.username} and {self.fullname} are manadatory")

    def save_player(self):
        pass

