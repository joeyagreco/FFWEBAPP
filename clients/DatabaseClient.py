import os
import random

from dotenv import load_dotenv
from pymongo import MongoClient

from helpers.Error import Error

load_dotenv()


class DatabaseClient:

    def __init__(self):
        self.__cluster = MongoClient(os.getenv("DATABASE_CLUSTER"))
        self.__database = self.__cluster[os.getenv("DATABASE_DATABASE")]
        self.__collection = self.__database[os.getenv("DATABASE_COLLECTION")]

    def __generateLeagueId(self):
        """
        Returns a new and unused random league id
        Will be between 100000-999999 [always 6 digits]
        """
        newLeagueId = random.randint(100000, 999999)
        while self.__collection.find_one({"_id": newLeagueId}):
            newLeagueId = random.randint(100000, 999999)
        return newLeagueId

    def getLeague(self, leagueId):
        """
        Returns a Document object or an Error object if not inserted
        https://docs.mongodb.com/manual/reference/method/db.collection.findOne/
        """
        response = self.__collection.find_one({"_id": leagueId})
        if response:
            return response
        else:
            return Error(f"Could not find a league with ID: {leagueId}")

    def addLeague(self, leagueName: str, numberOfTeams: int):
        """
        Adds a league with a new generated ID to the database
        Returns a Document object or an Error object if not inserted
        https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
        """
        league = {"_id": self.__generateLeagueId(), "leagueName": leagueName,
                  "numberOfTeams": numberOfTeams, "weeks": []}
        response = self.__collection.insert_one(league)
        if response:
            return response
        else:
            return Error("Could not insert into database.")
