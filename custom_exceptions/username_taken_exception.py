

class UsernameTakenException(Exception):
    def __init__(self, message='username taken'):
        self.message = message