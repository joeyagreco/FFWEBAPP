from clients.DatabaseClient import DatabaseClient
from helpers.Error import Error
from packages.Verifiers.DatabaseVerifier import DatabaseVerifier


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

    def updateLeague(self, leagueId: int, leagueName: str, teams: list, weeks: list):
        """
        Does checks on the updated league data
        Either passes the request to the client or returns an Error
        """
        databaseVerifier = DatabaseVerifier()
        if databaseVerifier.duplicateTeamNames(teams):
            return Error("Duplicate team names.")
        else:
            return self.__databaseClient.updateLeague(leagueId, leagueName, teams, weeks)

    def deleteLeague(self, leagueId: int):
        return self.__databaseClient.deleteLeague(leagueId)
