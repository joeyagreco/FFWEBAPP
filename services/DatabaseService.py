from builders.LeagueBuilder import LeagueBuilder
from clients.DatabaseClient import DatabaseClient
from helpers.Error import Error
from packages.Verifiers.DatabaseVerifier import DatabaseVerifier
from packages.Verifiers.LeagueDictVerifier import LeagueDictVerifier


class DatabaseService:
    """
    This class connects the DatabaseClient to the main Controller.
    It contains logic where the client and controller can/should not.
    """

    def __init__(self):
        self.__databaseClient = DatabaseClient()

    def getLeague(self, leagueId):
        return self.__databaseClient.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int):
        # build out the teams list with default team names
        teams = []
        for x in range(1, numberOfTeams + 1):
            teams.append({"teamId": x, "teamName": f"Team {x}"})
        return self.__databaseClient.addLeague(leagueName, numberOfTeams, teams)

    def updateLeague(self, leagueId: int, leagueName: str, years):
        """
        Does checks on the updated league data
        Either passes the request to the client or returns an Error
        """
        if DatabaseVerifier.duplicateTeamNames(years):
            return Error("Duplicate team names.")
        if LeagueDictVerifier.teamPlaysItself(years):
            return Error("A team cannot play itself.")
        if LeagueDictVerifier.teamPlaysTwice(years):
            return Error("A team can not play twice in the same week.")
        return self.__databaseClient.updateLeague(leagueId, leagueName, years)

    def deleteLeague(self, leagueId: int):
        return self.__databaseClient.deleteLeague(leagueId)

    def deleteWeek(self, leagueId: int):
        return self.__databaseClient.deleteWeek(leagueId)

    def getLeagueModel(self, leagueId: int):
        """
        This takes in a league ID
        It returns a Python object version of the given league or an Error
        """
        leagueDict = self.__databaseClient.getLeague(leagueId)
        leagueBuilder = LeagueBuilder(leagueDict)
        return leagueBuilder.getLeagueObject()
