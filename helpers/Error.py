class Error:
    """
    This class is used to create general errors that are passed up to the main Flask app to display error messages on the front end to the user.
    """

    def __init__(self, errorMessage: str):
        self.__errorMessage = errorMessage

    def errorMessage(self) -> str:
        return self.__errorMessage
