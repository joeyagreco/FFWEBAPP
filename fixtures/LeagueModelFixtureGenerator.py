from models.LeagueModel import LeagueModel
from models.MatchupModel import MatchupModel
from models.TeamModel import TeamModel
from models.WeekModel import WeekModel


class LeagueModelFixtureGenerator:

    def __init__(self):
        pass

    def getDummyTeam(self):
        return TeamModel(1, "dummyTeam")

    def getDummyMatchup(self):
        return MatchupModel(self.getDummyTeam(), self.getDummyTeam(), 100.0, 100.0)

    def getDummyWeek(self):
        return WeekModel(1, [self.getDummyMatchup(), self.getDummyMatchup(), self.getDummyMatchup()])

    def getDummyLeague(self):
        return LeagueModel(100000, "dummyLeague", 6, self.getDummyWeek())
