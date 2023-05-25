from core.dotenv import config

class Settings():
	""" Utils settings using environements variables
	"""
	API_V1: str = config["API_V1"]
	PROJECT_NAME: str = config["PROJECT_NAME"]
	BACKEND_CORS_ORIGINS: str = config["BACKEND_CORS_ORIGINS"]
	MONGO_URI: str = config["MONGO_URI"]
	MONGO_DB_NAME: str = config["MONGO_DB_NAME"]
	SECRET_JWT_KEY: str = config["SECRET_JWT_KEY"]
	ACCESS_TOKEN_EXPIRE_MINUTES: int = int(config["ACCESS_TOKEN_EXPIRE_MINUTES"])
	ENCODE_ALGORITHM: str = config["ENCODE_ALGORITHM"]
	TOKEN_INFLUX: str = config["TOKEN_INFLUX"]
	ORG_INFLUX: str = config["ORG_INFLUX"]
	URL_INFLUX: str = config["URL_INFLUX"]
	BUCKET_INFLUX: str = config["BUCKET_INFLUX"]


settings = Settings()