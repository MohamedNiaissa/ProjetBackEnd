import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from core.config import settings

token = settings.TOKEN_INFLUX
org = settings.ORG_INFLUX
url = settings.URL_INFLUX
bucket = settings.BUCKET_INFLUX

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)


request_counter = {}


def log_request(route, response_time):
    if route in request_counter:
        request_counter[route] += 1
    else:
        request_counter[route] = 1


    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = (
        Point("request_stats")
        .tag("route", route)
        .field("counter", request_counter[route])
        .field("response_time", response_time)
    )

    write_api.write(bucket=bucket, org="kev", record=point)


class RequestStatsMiddleware(BaseHTTPMiddleware):
    @staticmethod
    async def dispatch(request: Request, call_next):

        route = request.url.path

        start_time = time.time()
        response = await call_next(request)
        end_time = time.time()
        # We can send time not converted and it converts in influxdb
        response_time = end_time - start_time
        # send time directly in ms
        current_time_millis = int(round(response_time * 1000))

        log_request(route, current_time_millis)
        return response
