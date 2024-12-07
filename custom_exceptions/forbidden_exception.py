

class ForbiddenException(Exception):
    def __init__(self, message='forbidden'):
        super(ForbiddenException, self).__init__(message)
        self.message = message