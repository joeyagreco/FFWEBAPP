class LeagueDictVerifier:
    """
    This class is used check a league Dictionary to ensure it is well formed.
    """

    def teamPlaysItself(self, weeks: list) -> bool:
        """
        Returns a boolean of whether any teams play themselves in the given weeks.
        """
        for week in weeks:
            for matchup in week["matchups"]:
                if matchup["teamA"]["teamId"] == matchup["teamB"]["teamId"]:
                    return True
        return False

    def teamPlaysTwice(self, weeks: list) -> bool:
        """
        Returns a boolean of whether a team plays twice in any week in the given weeks.
        """
        for week in weeks:
            teamIdsThatHavePlayed = []
            for matchup in week["matchups"]:
                teamIdsThatHavePlayed.append(matchup["teamA"]["teamId"])
                teamIdsThatHavePlayed.append(matchup["teamB"]["teamId"])
            teamIdsSet = set(teamIdsThatHavePlayed)
            if len(teamIdsThatHavePlayed) != len(teamIdsSet):
                return True
        return False
