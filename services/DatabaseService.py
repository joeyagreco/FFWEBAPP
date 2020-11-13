from clients.DatabaseClient import DatabaseClient


class DatabaseService:

    def __init__(self):
        self.__databaseClient = DatabaseClient()

    def getLeague(self, leagueId):
        return self.__databaseClient.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int):
        # build out the teams list
        teams = []
        for x in range(1, numberOfTeams + 1):
            teams.append({"teamId": x, "teamName": ""})
        return self.__databaseClient.addLeague(leagueName, numberOfTeams, teams)

    def updateLeague(self, leagueId: int, leagueName: str, teams: list):
        return self.__databaseClient.updateLeague(leagueId, leagueName, teams)

    def deleteLeague(self, leagueId: int):
        return self.__databaseClient.deleteLeague(leagueId)
