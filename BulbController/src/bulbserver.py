import asyncio
import os
import json
from threading import Thread
from flask import Flask, Response, request
from flask_cors import CORS
from utils import LightingRequest, log
from bulb import BulbController
from gevent.pywsgi import WSGIServer

# Flask app object with CORS
app: Flask = Flask("__main__")
CORS(app)

# Global bulb controllers
bulb_1: BulbController = BulbController()
bulb_2: BulbController = BulbController()

# Event loop for running bulb commands in a seperate thread
loop = asyncio.new_event_loop()


@app.route("/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/lightingrequest/bulb1", methods=["POST"])
async def lighting_request_bulb_1() -> Response:
    bulb_request = LightingRequest(**json.loads(request.data))
    log(bulb_request.__dict__)

    bulb_1.request = bulb_request
    asyncio.run_coroutine_threadsafe(bulb_1.bulb.update(), loop)
    asyncio.run_coroutine_threadsafe(
        bulb_1.operation_callback_by_name[bulb_request.operation](), loop
    )
    return Response(status=200)


@app.route("/lightingrequest/bulb2", methods=["POST"])
async def lighting_request_bulb_2() -> Response:
    bulb_request = LightingRequest(**json.loads(request.data))
    log(bulb_request.__dict__)

    bulb_2.request = bulb_request
    asyncio.run_coroutine_threadsafe(bulb_2.bulb.update(), loop)
    asyncio.run_coroutine_threadsafe(
        bulb_2.operation_callback_by_name[bulb_request.operation](), loop
    )
    return Response(status=200)


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    bulb_thread = Thread(target=start_background_loop, args=(loop,), daemon=True)
    bulb_thread.start()

    asyncio.run_coroutine_threadsafe(bulb_1.create_bulb(os.environ["BULB_1_IP"]), loop)
    asyncio.run_coroutine_threadsafe(bulb_2.create_bulb(os.environ["BULB_2_IP"]), loop)

    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
