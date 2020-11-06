from clients.DatabaseClient import DatabaseClient


class DatabaseService:

    def __init__(self):
        self.__databaseClient = DatabaseClient()

    def getLeague(self, leagueId):
        return self.__databaseClient.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int):
        return self.__databaseClient.addLeague(leagueName, numberOfTeams)
