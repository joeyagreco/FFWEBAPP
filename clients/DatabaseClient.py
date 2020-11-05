import pymongo
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import random
import os

load_dotenv()


class DatabaseClient:

    def __init__(self):
        self.__cluster = MongoClient(os.getenv("DATABASE_CLUSTER"))
        self.__database = self.__cluster[os.getenv("DATABASE_DATABASE")]
        self.__collection = self.__database[os.getenv("DATABASE_COLLECTION")]

    def __generateLeagueId(self):
        """ Returns a new and unused random league id """
        newLeagueId = random.randint(1, 1000000)
        while self.__collection.find_one({"_id": newLeagueId}):
            newLeagueId = random.randint(1, 1000000)
        return newLeagueId

    def getLeague(self, leagueId):
        return self.__collection.find_one({"_id": leagueId})

    def addLeague(self):
        """
        example data
        post = {"_id":0, *leagueJsonHere}
        """
        league = {"_id": self.__generateLeagueId()}
        return self.__collection.insert_one(league)
        print("posted successfully")
