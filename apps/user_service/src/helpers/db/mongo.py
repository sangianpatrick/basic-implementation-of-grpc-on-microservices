from pymongo import MongoClient
from config import MONGO_DB


class MongoDB():
    def __init__(self, host, db):
        self.host = host
        self.client = MongoClient(self.host)
        self.db = self.client[db]

    @staticmethod
    def obj_id_to_string(item):
        item['_id'] = str(item['_id'])
        return item

    def insert_one(self, collection,**document):
      collection = self.db[collection]
      result = collection.insert_one(document)
      return result

    def find_all(self, collection, condition, options):
        collection = self.db[collection]
        result = collection.find(condition, options)
        return list(result)
    
    def find_one(self, collection, condition, options):
      collection = self.db[collection]
      result = collection.find_one(condition, options)
      return result

    def upsert_one(self, collection, condition, document):
      collection = self.db[collection]
      upsert = collection.replace_one(condition, document, True)
      if upsert.matched_count < 1:
        return None
      return 1
    
    def delete_one(self, collection, condition):
      collection = self.db[collection]
      delete = collection.delete_one(condition)
      if delete.deleted_count < 1:
        return None
      return 1