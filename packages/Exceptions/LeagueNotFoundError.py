class LeagueNotFoundError(Exception):
    """
    Exception raised when a league is not found.
    """

    def __init__(self, message: str):
        super().__init__(message)
