import pymongo
from pymongo import MongoClient


class TestDatabase:

    def __init__(self):
        self.cluster = MongoClient("mongodb://127.0.0.1:27017/")
        self.db = self.cluster["TestDatabase"]
        self.collection = self.db["TestCollection"]
        print("created db instance")

    def post(self, id, data):
        # example data
        # post = {"_id":0, "name":"joey", "age":23}

        data["_id"] = id
        self.collection.insert_one(data)
        print("posted successfully")
