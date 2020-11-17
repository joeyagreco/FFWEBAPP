class LeagueModelFixtureGeneratorDict:

    def __init__(self):
        pass

    def getDummyTeamDict(self):
        return {"teamId": 1, "teamName": "dummyTeam"}

    def getDummyMatchupDict(self):
        return {"matchupId": 1, "teamA": self.getDummyTeamDict(), "teamB": self.getDummyTeamDict(),
                "teamAScore": 100.0, "teamBScore": 100.0}

    def getDummyWeekDict(self):
        return {"weekNumber": 1,
                "matchups": [self.getDummyMatchupDict(), self.getDummyMatchupDict(), self.getDummyMatchupDict()]}

    def getDummyLeagueDict(self):
        return {"leagueId": 100000, "leagueName": "dummyLeague", "numberOfTeams": 6,
                "teams": [self.getDummyTeamDict(), self.getDummyTeamDict(), self.getDummyTeamDict(),
                          self.getDummyTeamDict(), self.getDummyTeamDict(), self.getDummyTeamDict()],
                "weeks": self.getDummyWeekDict()}
