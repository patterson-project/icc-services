import asyncio
from threading import Thread
from utils import initialize_led_strips, start_background_loop
from repository import AnalyticsRepository, DeviceRepository, StateRepository
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from kasa import SmartDeviceException
from ledstrip import LedStrip
from gevent.pywsgi import WSGIServer
from icc.models import PydanticObjectId, LightingRequestDto


""" Flask and Repository Setup """

app = Flask("__main__")
CORS(app)

device_repository: DeviceRepository = DeviceRepository(app)
state_repository: StateRepository = StateRepository(app)
analytics_repository: AnalyticsRepository = AnalyticsRepository(app)


""" Led Strips and Asyncio Event Loop """

loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
global led_strips
led_strips: dict[PydanticObjectId, LedStrip] = initialize_led_strips(
    device_repository, loop)


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
def update_led_strips() -> Response:
    global led_strips
    led_strips = initialize_led_strips(device_repository, loop)
    return "Success", 200


@app.route("/request", methods=["POST"])
def lighting_request() -> Response:
    try:
        lighting_request = LightingRequestDto(**request.get_json())
        led_strip_controller = led_strips[lighting_request.target]
        led_strip_controller.set_request(lighting_request)

        asyncio.run_coroutine_threadsafe(
            led_strip_controller.operation_callback_by_name[lighting_request.operation](
            ), loop
        )

        state: bool = False
        if lighting_request.operation != "off":
            state = True

        state_repository.update(lighting_request.target, state)
        analytics_repository.save(lighting_request.target, state)

        return "Success", 200

    except (SmartDeviceException, TypeError, KeyError) as e:
        return str(e), 500


if __name__ == "__main__":
    strip_thread = Thread(target=start_background_loop,
                          args=(loop,), daemon=True)
    strip_thread.start()

    http_server = WSGIServer(("", 8000), app)
    http_server.serve_forever()
