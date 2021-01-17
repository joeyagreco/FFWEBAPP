class InvalidTeamForStatError(Exception):
    """
    Exception raised when a stat is calculated for a team for which that stat is not applicable.
    """

    def __init__(self, message: str):
        super().__init__(message)
