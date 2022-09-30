import asyncio
from threading import Thread
from objectid import PydanticObjectId
from utils import initialize_bulbs
from repository import DeviceRepository, StateRepository, AnalyticsRepository
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from kasa import SmartDeviceException
from lightingrequest import LightingRequest
from bulb import Bulb
from gevent.pywsgi import WSGIServer


""" Flask and Repository Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
state_repository: StateRepository = StateRepository(app)
analytics_repository: AnalyticsRepository = AnalyticsRepository(app)


""" Bulbs and Asyncio Event Loop """

loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
bulbs: dict[PydanticObjectId, Bulb] = initialize_bulbs(device_repository, loop)


""" Error Handler """

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


""" Health """

@app.route("/health")
def index() -> Response:
    return "Healthy", 200


""" Bulb Requests"""

@app.route("/update", methods=["PUT"])
def update_bulbs() -> Response:
    bulbs.clear()
    bulbs = initialize_bulbs(device_repository, loop)
    return "Success", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequest(**request.get_json())
        bulb_controller = bulbs[lighting_request.target]
        bulb_controller.set_request(lighting_request)
        asyncio.run_coroutine_threadsafe(
            bulb_controller.operation_callback_by_name[lighting_request.operation](
            ), loop
        )

        state: bool = None
        if lighting_request.operation != "off":
            state = True
        else:
            state = False

        state_repository.update(lighting_request.target, state)
        analytics_repository.save(lighting_request.target, state)

        return "Success", 200

    except (SmartDeviceException, TypeError, KeyError) as e:
        return str(e), 500


def start_background_loop(loop: asyncio.AbstractEventLoop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


if __name__ == "__main__":
    bulb_thread = Thread(target=start_background_loop,
                         args=(loop,), daemon=True)
    bulb_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
