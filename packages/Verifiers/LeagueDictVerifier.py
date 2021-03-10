class LeagueDictVerifier:
    """
    This class is used check a league Dictionary to ensure it is well formed.
    """

    @staticmethod
    def teamPlaysItself(years: dict) -> bool:
        """
        Returns a boolean of whether any teams play themselves in the given weeks.
        """
        for year in years:
            # check if its year 0
            if year != str(0):
                for week in years[year]["weeks"]:
                    for matchup in week["matchups"]:
                        if matchup["teamA"]["teamId"] == matchup["teamB"]["teamId"]:
                            return True
        return False

    @staticmethod
    def teamPlaysTwice(years: dict) -> bool:
        """
        Returns a boolean of whether a team plays twice in any week in the given weeks.
        """
        for year in years.keys():
            # check if its year 0
            if year != str(0):
                for week in years[year]["weeks"]:
                    teamIdsThatHavePlayed = []
                    for matchup in week["matchups"]:
                        teamIdsThatHavePlayed.append(matchup["teamA"]["teamId"])
                        teamIdsThatHavePlayed.append(matchup["teamB"]["teamId"])
                    teamIdsSet = set(teamIdsThatHavePlayed)
                    if len(teamIdsThatHavePlayed) != len(teamIdsSet):
                        return True
        return False
