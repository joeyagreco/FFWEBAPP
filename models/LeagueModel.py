from typing import List

from models import WeekModel


class LeagueModel:

    def __init__(self, leagueId: int, name: str, numberOfTeams: int, weeks: List[WeekModel]):
        self.__leagueId = leagueId
        self.__name = name
        self.__numberOfTeams = numberOfTeams
        self.__weeks = weeks

    def getLeagueId(self):
        return self.__leagueId

    def getName(self):
        return self.__name

    def getNumberOfTeams(self):
        return self.__numberOfTeams

    def getWeeks(self):
        return self.__weeks