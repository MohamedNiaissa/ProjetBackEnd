from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.api import api_router
from core.config import settings
from mongo.init_db import client

app = FastAPI()

@app.on_event("shutdown")
def shutdown_db_client():
    client.close()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
	app.add_middleware(
		CORSMiddleware,
		allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

app.include_router(api_router, prefix=settings.API_V1)