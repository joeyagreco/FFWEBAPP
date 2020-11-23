from typing import List

from models.league_stat_models import LeagueStatMarginOfVictoryModel, LeagueStatScoreModel


class LeagueStatsModel:

    def __init__(self, allMarginsOfVictory: List[LeagueStatMarginOfVictoryModel],
                 allScores: List[LeagueStatScoreModel]):
        self.__allMarginsOfVictory = allMarginsOfVictory
        self.__allScores = allScores

    def getAllMarginsOfVictory(self):
        return self.__allMarginsOfVictory

    def getAllScores(self):
        return self.__allScores
