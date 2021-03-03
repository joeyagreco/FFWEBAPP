from typing import List

from models.league_models.LeagueModel import LeagueModel
from models.league_stat_models.StreakModel import StreakModel


class StreakCalculator:

    def __init__(self, leagueModel: LeagueModel, teamId: int, years: list):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__years = years

    def getWinStreaks(self) -> List[StreakModel]:
        """
        This returns a list of StreakModels that contain all the win streaks for the team with self.__teamId in self.__leagueModel within self.__years.
        """
        return None