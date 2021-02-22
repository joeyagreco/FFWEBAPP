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
        for year in league["years"]:
            if year["year"] == yearNumber:
                return year

    @staticmethod
    def updateYear(league: dict, newYear: dict) -> dict:
        """
        This replaces the dict in the given league with the year number of the given year with the given year dict.
        """
        for year in league["years"]:
            if year["year"] == newYear["year"]:
                league["years"].remove(year)
                league["years"].append(newYear)
                return newYear