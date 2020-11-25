from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.MaxScore import MaxScore
from packages.StatCalculators.MinScore import MinScore
from packages.StatCalculators.Ppg import Ppg


class StatCalculatorService:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getTeamStats(self):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        for team in self.__leagueModel.getTeams():
            minScoreCalculator = MinScore(team.getTeamId(), self.__leagueModel)
            print(minScoreCalculator.getMinScore())
            maxScoreCalculator = MaxScore(team.getTeamId(), self.__leagueModel)
            print(maxScoreCalculator.getMaxScore())
            ppgCalculator = Ppg(team.getTeamId(), self.__leagueModel)
            print(ppgCalculator.getPpg())

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

