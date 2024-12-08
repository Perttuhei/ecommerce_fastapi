class NotFoundException(Exception):
    def __init__(self, message='not found'):
        self.message = message