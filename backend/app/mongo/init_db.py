# import os
from pymongo import MongoClient
from core.config import settings

# os.environ["MONGO_URI"]
client = MongoClient(settings.MONGO_URI)