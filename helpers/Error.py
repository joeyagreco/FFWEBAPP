class Error:

    def __init__(self, errorMessage: str):
        self.__errorMessage = errorMessage

    def errorMessage(self) -> str:
        return f"ERROR: {self.__errorMessage}"
