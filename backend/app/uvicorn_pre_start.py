import logging
import uvicorn

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from mongo.init_db import client
from core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5
wait_seconds = 1


@retry(
	stop=stop_after_attempt(max_tries),
	wait=wait_fixed(wait_seconds),
	before=before_log(logger, logging.INFO),
	after=after_log(logger, logging.WARN),
)
def init() -> None:
	try:
		# Try to create client and db to check if awake
		client.server_info()
	except Exception as e:
		logger.error(e)
		raise e


def checkMongoClient() -> None:
	logger.info("Initializing service")
	init()
	logger.info("Service finished initializing")


async def app(scope, receive, send) -> None:
	...

if __name__ == "__main__":
	checkMongoClient()

	conf = uvicorn.Config("main:app", port=8080, reload=True, log_level="info")
	server = uvicorn.Server(conf)
	server.run()