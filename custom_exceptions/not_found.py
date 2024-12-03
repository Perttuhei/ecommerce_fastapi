class NotFound(Exception):
    def __init__(self, message='not found'):
        self.message = message