class LeagueDictVerifier:

    def teamPlaysItself(self, weeks: list):
        """
        Returns a boolean of whether the given week has any teams that play themselves
        """
        for week in weeks:
            for matchup in week["matchups"]:
                if matchup["teamA"]["teamId"] == matchup["teamB"]["teamId"]:
                    return True
        return False
