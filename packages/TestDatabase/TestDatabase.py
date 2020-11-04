import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


class TestDatabase:

    def __init__(self):
        self.cluster = MongoClient(os.getenv("DATABASE_CLUSTER"))
        self.database = self.cluster[os.getenv("DATABASE_DATABASE")]
        self.collection = self.database[os.getenv("DATABASE_COLLECTION")]
        print("created db instance")

    def post(self, id, data):
        # example data
        # post = {"_id":0, "name":"joey", "age":23}

        data["_id"] = id
        self.collection.insert_one(data)
        print("posted successfully")
