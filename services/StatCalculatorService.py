from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.MinMaxScoreCalculator import MinMaxScoreCalculator
from packages.StatCalculators.PpgCalculator import Ppg


class StatCalculatorService:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getTeamStats(self):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        for team in self.__leagueModel.getTeams():
            minMaxScoreCalculator = MinMaxScoreCalculator(team.getTeamId(), self.__leagueModel)
            print(minMaxScoreCalculator.getMinScore())
            print(minMaxScoreCalculator.getMaxScore())
            ppgCalculator = Ppg(team.getTeamId(), self.__leagueModel)
            print(ppgCalculator.getPpg())

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

