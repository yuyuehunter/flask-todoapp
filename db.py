from pymongo import MongoClient

class Database(object):
    def __init__(self, db_name, host='localhost', port=27017):
        self.client = MongoClient()

        self.db = self.client[db_name]
