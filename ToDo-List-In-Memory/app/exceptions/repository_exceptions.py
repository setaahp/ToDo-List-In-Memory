from .base import ToDoException

class NotFoundException(ToDoException):
    pass

class AlreadyExistsException(ToDoException):
    pass
