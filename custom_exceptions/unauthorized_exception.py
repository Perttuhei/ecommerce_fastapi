

class UnauthorizedException(Exception):
    def __init__(self, message='login is required'):
        super(UnauthorizedException, self).__init__(message)
        self.message = message