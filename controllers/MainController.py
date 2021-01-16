from models.league_models.LeagueModel import LeagueModel
from services.DatabaseService import DatabaseService
from services.StatCalculatorService import StatCalculatorService


class MainController:
    """
    This class is used to connect the main Flask app to existing services.
    """

    def __init__(self):
        self.__databaseService = DatabaseService()
        self.__statCalculatorService = StatCalculatorService()

    def getLeague(self, leagueId: int):
        return self.__databaseService.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int):
        return self.__databaseService.addLeague(leagueName, numberOfTeams)

    def updateLeague(self, leagueId: int, leagueName: str, teams: list, weeks: list):
        return self.__databaseService.updateLeague(leagueId, leagueName, teams, weeks)

    def deleteLeague(self, leagueId: int):
        return self.__databaseService.deleteLeague(leagueId)

    def deleteWeek(self, leagueId: int):
        return self.__databaseService.deleteWeek(leagueId)

    def getLeagueModel(self, leagueId: int):
        return self.__databaseService.getLeagueModel(leagueId)

    def getTeamStatsModel(self, leagueModel: LeagueModel):
        return self.__statCalculatorService.getTeamStats(leagueModel)

    def getHeadToHeadStatsModel(self, leagueModel: LeagueModel, team1Id: int, team2Id: int):
        return self.__statCalculatorService.getHeadToHeadStats(leagueModel, team1Id, team2Id)

    def getLeagueStatsModel(self, leagueModel: LeagueModel, statSelection: str):
        return self.__statCalculatorService.getLeagueStats(leagueModel, statSelection)

