import pymongo
from pymongo import MongoClient


class DatabaseClient:

    def __init__(self, leagueId):
        self.__leagueId = leagueId
        self.__cluster = MongoClient("mongodb://127.0.0.1:27017/")
        self.__database = self.cluster["TestDatabase"]
        self.__collection = self.db["TestCollection"]
