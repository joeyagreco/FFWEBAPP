class LeagueDictNavigator:
    """
    This class is used to navigate a dict representation of a league.
    # TODO test this class
    """

    @staticmethod
    def getYear(league: dict, yearNumber: int) -> dict:
        """
        This returns a dict of the given year
        """
        print(league)
        for year in league["years"]:
            if year["year"] == yearNumber:
                return year
