from core.dotenv import config

class Settings():
	API_V1: str = config["API_V1"]
	PROJECT_NAME: str = config["PROJECT_NAME"]
	BACKEND_CORS_ORIGINS: str = config["BACKEND_CORS_ORIGINS"]
	MONGO_URI: str = config["MONGO_URI"]
	MONGO_DB_NAME: str = config["MONGO_DB_NAME"]


settings = Settings()