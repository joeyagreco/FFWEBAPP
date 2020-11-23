from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.Ppg import Ppg


class StatCalculatorService:

    def __init__(self, leagueModel: LeagueModel):
        self.__leagueModel = leagueModel

    def getTeamStats(self):
        """
        Returns a list of TeamStatsModels, one for each team in the given league.
        """
        ppgCalculator = Ppg(1, self.__leagueModel)
        return ppgCalculator.getPpg()

    def getLeagueStats(self):
        """
        Returns a LeagueStatsModel for the given league.
        """
        return None

