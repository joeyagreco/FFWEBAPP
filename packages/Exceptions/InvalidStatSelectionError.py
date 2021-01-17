class InvalidStatSelectionError(Exception):
    """
    Exception raised when a stat that does not exist is attempted to be calculated.
    """

    def __init__(self, message: str):
        super().__init__(message)
