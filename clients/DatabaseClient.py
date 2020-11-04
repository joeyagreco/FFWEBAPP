import pymongo
from bson import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import random
import os

load_dotenv()


class DatabaseClient:

    def __init__(self, leagueId):
        self.__leagueId = leagueId
        self.__cluster = MongoClient(os.getenv("DATABASE_CLUSTER"))
        self.__database = self.__cluster[os.getenv("DATABASE_DATABASE")]
        self.__collection = self.__database[os.getenv("DATABASE_COLLECTION")]

    def getLeague(self):
        return self.__collection.find_one({"_id": self.__leagueId})

    def setLeague(self, leagueId, league):
        """
        example data
        post = {"_id":0, *leagueJsonHere}
        """

        league["_id"] = leagueId
        self.__collection.insert_one(league)
        print("posted successfully")
