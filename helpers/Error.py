class Error:

    def __init__(self, errorMessage: str):
        self.__errorMessage = errorMessage

    def errorMessage(self):
        return f"ERROR: {self.__errorMessage}"
