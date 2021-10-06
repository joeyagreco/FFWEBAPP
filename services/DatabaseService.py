from builders.LeagueBuilder import LeagueBuilder
from clients.DatabaseClient import DatabaseClient
from models.league_models.LeagueModel import LeagueModel
from packages.Exceptions.LeagueNotWellFormedError import LeagueNotWellFormedError
from packages.Verifiers.LeagueDictVerifier import LeagueDictVerifier


class DatabaseService:
    """
    This class connects the DatabaseClient to the main Controller.
    It contains logic where the client and controller can/should not.
    """

    def __init__(self):
        self.__databaseClient = DatabaseClient()

    def getLeague(self, leagueId) -> dict:
        # Returns the league with the given ID
        # Raises a LeagueNotFoundError if the league cannot be found
        return self.__databaseClient.getLeague(leagueId)

    def addLeague(self, leagueName: str, numberOfTeams: int) -> int:
        """
        Returns the added league's ID
        Raises a DatabaseError if the league cannot be found
        """
        # build out the teams list with default team names
        teams = []
        for x in range(1, numberOfTeams + 1):
            teams.append({"teamId": x, "teamName": f"Team {x}"})
        return self.__databaseClient.addLeague(leagueName, numberOfTeams, teams)

    def updateLeague(self, leagueId: int, leagueName: str, years):
        """
        Returns a Document object
        Raises a DatabaseError if the league could not be updated
        Raises a LeagueNotWellFormedError if there is an issue with league formatting
        Does checks on the updated league data
        """
        if LeagueDictVerifier.duplicateTeamNames(years):
            raise LeagueNotWellFormedError("Duplicate team names.")
        if LeagueDictVerifier.teamPlaysItself(years):
            raise LeagueNotWellFormedError("A team cannot play itself.")
        if LeagueDictVerifier.teamPlaysTwice(years):
            raise LeagueNotWellFormedError("A team cannot play twice in the same week.")
        return self.__databaseClient.updateLeague(leagueId, leagueName, years)

    def deleteLeague(self, leagueId: int) -> None:
        # Raises a DatabaseError if the league could not be deleted
        return self.__databaseClient.deleteLeague(leagueId)

    def deleteWeek(self, leagueId: int, year: int) -> dict:
        """
        Returns the league as a dictionary if successfully deleted
        Raises a DatabaseError if the week could not be deleted
        Raises a LeagueNotFoundError if the league could not be found
        """
        return self.__databaseClient.deleteWeek(leagueId, year)

    def getLeagueModel(self, leagueId: int) -> LeagueModel:
        """
        This takes in a league ID
        It returns the league model of the league with the given ID
        Raises a DatabaseError if the league cannot be found
        """
        leagueDict = self.__databaseClient.getLeague(leagueId)
        leagueBuilder = LeagueBuilder(leagueDict)
        return leagueBuilder.getLeagueObject()
