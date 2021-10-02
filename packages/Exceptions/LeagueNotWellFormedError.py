class LeagueNotWellFormedError(Exception):
    """
    Exception raised when a league is not well formed.
    """

    def __init__(self, message: str):
        super().__init__(message)
