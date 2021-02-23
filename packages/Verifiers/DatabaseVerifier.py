class DatabaseVerifier:
    """
    This class is used to verify data before it is placed into the database.
    """

    @staticmethod
    def duplicateTeamNames(years: dict) -> bool:
        """
        Returns a boolean of whether the given years dict has any years duplicate team names.
        """
        for year in years.keys():
            teamNames = []
            for team in years[year]["teams"]:
                teamNames.append(team["teamName"].lower().strip())
            teamNamesSet = set(teamNames)
            if len(teamNames) != len(teamNamesSet):
                return True
        return False
