from helpers import MongoDB
from config import MONGO_DB
from bson.objectid import ObjectId


class User():
    collection = 'users'

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def save(self):
        user = self.__repr__()
        condition = {
            '$or': [
                {'email': user['email']},
                {'user_id': user['user_id']}
            ]
        }
        check_user = User.get(condition)
        if not check_user is None:
            return 0
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        result = db.insert_one(self.collection, **self.__repr__())
        print(result.inserted_id)
        return 1

    @staticmethod
    def get_all(condition, **options):
        if not bool(options):
            options = None
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        return db.find_all(User.collection, condition, options)

    @staticmethod
    def get_by_id(user_id, **options):
        if not bool(options):
            options = None
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        return db.find_one(User.collection, {'user_id': user_id}, options)

    @staticmethod
    def get(condition, **options):
        if not bool(options):
            options = None
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        return db.find_one(User.collection, condition, options)

    @staticmethod
    def upsert(condition, document):
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        return db.upsert_one(User.collection, condition, document)
    
    @staticmethod
    def delete(condition):
        db = MongoDB(MONGO_DB['host'], MONGO_DB['db'])
        return db.delete_one(User.collection, condition)

    def __repr__(self):
        return self.__dict__
