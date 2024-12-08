
class CategoryExistsException(Exception):
    def __init__(self, message='category already exists'):
        self.message = message
