import asyncio
import json
from threading import Thread
from flask import Flask, Response, request
from flask_cors import CORS
from utils import LightingRequest, log
from bulb import BulbController
from gevent.pywsgi import WSGIServer

app: Flask = Flask("__main__")
CORS(app)

bulb_controller: BulbController = BulbController()
loop = asyncio.new_event_loop()


@app.route("/health")
def index() -> Response:
    return Response("Healthy", status=200)


@app.route("/lightingrequest", methods=["POST"])
async def lighting_request() -> Response:
    bulb_request = LightingRequest(**json.loads(request.data))
    log(bulb_request.__dict__)

    bulb_controller.request = bulb_request
    asyncio.run_coroutine_threadsafe(bulb_controller.bulb.update(), loop)
    asyncio.run_coroutine_threadsafe(
        bulb_controller.operation_callback_by_name[bulb_request.operation](), loop
    )
    return Response(status=200)


def start_background_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    bulb_thread = Thread(target=start_background_loop, args=(loop,), daemon=True)
    bulb_thread.start()
    asyncio.run_coroutine_threadsafe(bulb_controller.create_bulb("10.0.0.37"), loop)
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
