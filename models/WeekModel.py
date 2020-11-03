from typing import List

from models import MatchupModel


class WeekModel:

    def __init__(self, weekNumber: int, matchups: List[MatchupModel]):
        self.__weekNumber = weekNumber
        self.__matchups = matchups

    def getWeekNumber(self):
        return self.__weekNumber

    def getMatchups(self):
        return self.__matchups
