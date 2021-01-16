class DatabaseVerifier:
    """
    This class is used to verify data before it is placed into the database.
    """

    def duplicateTeamNames(self, teams: list) -> bool:
        """
        Returns a boolean of whether the given team list has any duplicate team names.
        """
        teamNames = []
        for team in teams:
            teamNames.append(team["teamName"].lower().strip())
        teamNamesSet = set(teamNames)
        return len(teamNames) != len(teamNamesSet)
