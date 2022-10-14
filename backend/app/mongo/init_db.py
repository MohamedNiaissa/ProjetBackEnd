from typing import Generator
from pymongo import MongoClient
from core.config import settings

client = MongoClient(settings.MONGO_URI)

def get_db() -> Generator:
	""" Get database from mongo client

	Yields:
		Generator: yield database
	"""
	db = client[settings.MONGO_DB_NAME]
	yield db