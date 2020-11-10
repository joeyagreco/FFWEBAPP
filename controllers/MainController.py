from services.DatabaseService import DatabaseService


class MainController:

    def __init__(self):
        self.__databaseService = DatabaseService()

    def getLeague(self, leagueId: int):
        return self.__databaseService.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int, teams: list):
        return self.__databaseService.addLeague(leagueName, numberOfTeams, teams)

    def updateLeague(self, leagueId: int, leagueName: str, teams: list):
        return self.__databaseService.updateLeague(leagueId, leagueName, teams)

    def deleteLeague(self, leagueId: int):
        return self.__databaseService.deleteLeague(leagueId)

