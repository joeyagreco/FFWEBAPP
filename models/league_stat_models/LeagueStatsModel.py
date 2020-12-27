from typing import List

from models.league_stat_models import MarginOfVictoryModel, ScoreModel


class LeagueStatsModel:

    def __init__(self, allMarginsOfVictory: List[MarginOfVictoryModel],
                 allScores: List[ScoreModel]):
        self.__allMarginsOfVictory = allMarginsOfVictory
        self.__allScores = allScores

    def getAllMarginsOfVictory(self):
        return self.__allMarginsOfVictory

    def getAllScores(self):
        return self.__allScores
