import asyncio
from threading import Thread
from utils import initialize_plugs, start_background_loop
from repository import AnalyticsRepository, DeviceRepository, StateRepository
from objectid import PydanticObjectId
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from kasa import SmartDeviceException
from powerrequest import PowerRequest
from plug import Plug
from gevent.pywsgi import WSGIServer
from state import State


""" Flask and Repository Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
state_repository: StateRepository = StateRepository(app)
analytics_repository: AnalyticsRepository = AnalyticsRepository(app)


""" Plugs and Asyncio Event Loop """

loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
global plugs
plugs: dict[PydanticObjectId, Plug] = initialize_plugs(device_repository, loop)


""" Error Handler """

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


""" Health """

@app.route("/health")
def index() -> Response:
    return "Healthy", 200


""" Plug Requests"""

@app.route("/update", methods=["PUT"])
def update_bulbs() -> Response:
    global plugs
    plugs = initialize_plugs(device_repository, loop)
    return "Success", 200


@app.route("/request", methods=["POST"])
def plug_request() -> Response:
    try:
        power_request: PowerRequest = PowerRequest(**request.get_json())
        plug: Plug = plugs[power_request.target]
        plug.set_request(power_request)

        asyncio.run_coroutine_threadsafe(
            plug.operation_callback_by_name[power_request.operation](
            ), loop
        )

        state: bool = False
        if power_request.operation != "off":
            state = True

        state_repository.update(power_request.target, state)
        analytics_repository.save(power_request.target, state)

        return "Success", 200

    except (SmartDeviceException, TypeError, KeyError) as e:
        return str(e), 500


if __name__ == "__main__":
    strip_thread = Thread(target=start_background_loop,
                          args=(loop,), daemon=True)
    strip_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
