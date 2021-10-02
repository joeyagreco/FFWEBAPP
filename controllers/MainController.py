from typing import List

from models.headToHead_stat_models.HeadToHeadStatsModel import HeadToHeadStatsModel
from models.league_models.LeagueModel import LeagueModel
from models.team_stat_models.TeamStatsModel import TeamStatsModel
from services.DatabaseService import DatabaseService
from services.StatCalculatorService import StatCalculatorService


class MainController:
    """
    This class is used to connect the main Flask app to existing services.
    """

    def __init__(self):
        self.__databaseService = DatabaseService()

    def getLeague(self, leagueId: int) -> dict:
        return self.__databaseService.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int) -> int:
        return self.__databaseService.addLeague(leagueName, numberOfTeams)

    def updateLeague(self, leagueId: int, leagueName: str, years):
        return self.__databaseService.updateLeague(leagueId, leagueName, years)

    def deleteLeague(self, leagueId: int) -> None:
        return self.__databaseService.deleteLeague(leagueId)

    def deleteWeek(self, leagueId: int, year: int) -> dict:
        return self.__databaseService.deleteWeek(leagueId, year)

    def getLeagueModel(self, leagueId: int) -> LeagueModel:
        return self.__databaseService.getLeagueModel(leagueId)

    @staticmethod
    def getTeamStatsModel(leagueModel: LeagueModel, years: list) -> List[TeamStatsModel]:
        return StatCalculatorService.getTeamStats(leagueModel, years)

    @staticmethod
    def getHeadToHeadStatsModel(leagueModel: LeagueModel, year: list, team1Id: int, team2Id: int) -> List[
        HeadToHeadStatsModel]:
        return StatCalculatorService.getHeadToHeadStats(leagueModel, year, team1Id, team2Id)

    @staticmethod
    def getLeagueStatsModel(leagueModel: LeagueModel, years: list, statSelection: str):
        return StatCalculatorService.getLeagueStats(leagueModel, years, statSelection)

    @staticmethod
    def getGraphDiv(leagueModel: LeagueModel, years: list, screenWidth: float, graphSelection: str):
        return StatCalculatorService.getGraphDiv(leagueModel, years, screenWidth, graphSelection)
