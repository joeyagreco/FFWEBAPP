class DatabaseError(Exception):
    """
    Exception raised for various database errors.
    """

    def __init__(self, message: str):
        super().__init__(message)
