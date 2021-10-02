import os
import random
import ssl
from datetime import datetime

from dotenv import load_dotenv
from pymongo import MongoClient

from packages.Exceptions.DatabaseError import DatabaseError

load_dotenv()


class DatabaseClient:
    """
    This class is used to connect directly to the Mongo Database.
    """

    def __init__(self):
        self.__cluster = MongoClient(os.getenv("DATABASE_CLUSTER"), ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
        self.__database = self.__cluster[os.getenv("DATABASE_DATABASE")]
        self.__collection = self.__database[os.getenv("DATABASE_COLLECTION")]

    def __generateLeagueId(self) -> int:
        """
        Returns a new and unused random league id
        Will be between 100000-999999 [always 6 digits]
        """
        newLeagueId = random.randint(100000, 999999)
        while self.__collection.find_one({"_id": newLeagueId}):
            newLeagueId = random.randint(100000, 999999)
        return newLeagueId

    def getLeague(self, leagueId: int) -> dict:
        """
        Returns the league with the given ID
        Raises a DatabaseError if the league cannot be found
        https://docs.mongodb.com/manual/reference/method/db.collection.findOne/
        """
        response = self.__collection.find_one({"_id": leagueId})
        # response will be None if not found
        if response:
            return response
        else:
            raise DatabaseError(f"Could not find a league with ID: {leagueId}")

    def addLeague(self, leagueName: str, numberOfTeams: int, teams: list) -> int:
        """
        Adds a league with a new generated ID to the database
        Returns the new league's ID
        Raises a DatabaseError if the league could not be added
        https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
        """
        # set "year 0", which will be the "all time" year selection
        owners = []
        for i in range(1, len(teams) + 1):
            owners.append({"teamId": i, "teamName": f"Owner {i}"})
        year0 = {"year": 0, "teams": owners, "weeks": None}
        # get the current year and set it as default
        currentYear = datetime.now().year
        # construct default year object
        year = {"year": currentYear, "teams": teams, "weeks": []}
        league = {"_id": self.__generateLeagueId(),
                  "leagueName": leagueName,
                  "numberOfTeams": numberOfTeams,
                  "years": {"0": year0,
                            str(currentYear): year}}
        response = self.__collection.insert_one(league)
        if response.acknowledged:
            return response.inserted_id
        else:
            raise DatabaseError(f"Could not insert new league into database.")

    def updateLeague(self, leagueId: int, leagueName: str, years):
        """
        Updates a league with given parameters
        Returns a Document object
        Raises a DatabaseError if the league could not be updated
        https://docs.mongodb.com/manual/reference/method/db.collection.update/
        https://specify.io/how-tos/mongodb-update-documents
        """
        league = self.getLeague(leagueId)
        league["leagueName"] = leagueName
        league["years"] = years
        response = self.__collection.replace_one({"_id": leagueId}, league)
        if response:
            return response
        else:
            raise DatabaseError(f"Could not update league with ID: {leagueId}")

    def deleteLeague(self, leagueId: int) -> None:
        """
        Deletes the league with the given ID
        Raises a DatabaseError if the league could not be deleted
        https://docs.mongodb.com/manual/reference/method/db.collection.remove/
        """
        response = self.__collection.delete_one({"_id": leagueId})
        if response.deleted_count != 1:
            # could not delete the league
            raise DatabaseError(f"Could not delete league with ID: {leagueId}")

    def deleteWeek(self, leagueId: int, year: int) -> dict:
        """
        Deletes the most recent week of the year in the league with the given ID
        Returns the league as a dictionary if successfully deleted
        Raises a DatabaseError if the week could not be deleted
        https://docs.mongodb.com/manual/reference/method/db.collection.update/
        https://specify.io/how-tos/mongodb-update-documents
        """
        league = self.getLeague(leagueId)
        league["years"][str(year)]["weeks"] = league["years"][str(year)]["weeks"][:-1]
        response = self.__collection.replace_one({"_id": leagueId}, league)
        if response:
            league = self.getLeague(leagueId)
            return league
        else:
            raise DatabaseError(f"Could not delete week for league with ID: {leagueId}")
