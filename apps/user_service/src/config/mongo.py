
import os

MONGO_DB = {
    'host': os.environ['MONGODB_URL'],
    'db': os.environ['MONGODB_DATABASE']
}
