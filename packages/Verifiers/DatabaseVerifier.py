class DatabaseVerifier:

    def __init__(self):
        pass

    def duplicateTeamNames(self, teams: list):
        """
        Returns a boolean of whether the team list has any duplicate team names
        """
        teamNames = []
        for team in teams:
            teamNames.append(team["teamName"].lower().strip())
        teamNamesSet = set(teamNames)
        return len(teamNames) != len(teamNamesSet)
