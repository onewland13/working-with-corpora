
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class DataAccessError(Error):
    """Exception raised for errors in DataAccess.

    Attributes:
        operation -- operation in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

