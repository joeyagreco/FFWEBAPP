from typing import List

from models import WeekModel


class LeagueModel:

    def __init__(self, leagueId: int, leagueName: str, numberOfTeams: int, weeks: List[WeekModel]):
        self.__leagueId = leagueId
        self.__leagueName = leagueName
        self.__numberOfTeams = numberOfTeams
        self.__weeks = weeks

    def getLeagueId(self):
        return self.__leagueId

    def getLeagueName(self):
        return self.__leagueName

    def getNumberOfTeams(self):
        return self.__numberOfTeams

    def getWeeks(self):
        return self.__weeks
