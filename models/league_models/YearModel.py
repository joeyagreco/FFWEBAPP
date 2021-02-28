from typing import List

from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class YearModel:

    def __init__(self, year: int, teams: List[TeamModel], weeks: List[WeekModel]):
        self.__year = year
        self.__teams = teams
        self.__weeks = weeks

    def getYear(self):
        return self.__year

    def getTeams(self):
        return self.__teams

    def getWeeks(self):
        return self.__weeks
