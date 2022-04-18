import json
from multiprocessing.process import current_process
from kasa import SmartBulb
import paho.mqtt.client as mqtt
import led_operation
import asyncio
from rpi_ws281x import Adafruit_NeoPixel
from multiprocessing import Process
from utils import LedRequest, TerminalColors, LedConfig, log


class MqttClient:
    def __init__(self):
        self.strip = self.led_strip_init()
        self.client = self.mqtt_init()
        self.bulb_1 = SmartBulb('10.0.0.37')
        self.bulb_2 = SmartBulb('10.0.0.87')
        self.led_process = None

    def led_strip_init(self) -> Adafruit_NeoPixel:
        strip = Adafruit_NeoPixel(
            LedConfig.COUNT,
            LedConfig.PIN,
            LedConfig.FREQ_HZ,
            LedConfig.DMA,
            LedConfig.INVERT,
            LedConfig.BRIGHTNESS,
            LedConfig.CHANNEL,
        )
        strip.begin()
        return strip

    def mqtt_init(self) -> mqtt.Client:
        client = mqtt.Client("LedPi", clean_session=False)
        client.connect(LedConfig.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.subscribe("leds")
        return client

    async def bulb_init(self) -> None:
        await self.bulb_1.update()
        await self.bulb_2.update()

    def terminate_process(self) -> None:
        if self.led_process is not None:
            self.led_process.terminate()
            self.led_process.join()
            self.led_process = None

    def on_message(self, client, userdata, message) -> None:
        led_request = LedRequest(**json.loads(message.payload))
        log(message.topic, str(led_request.__dict__))

        try:
            # TODO manage this better
            if led_request.operation == "rgb":
                self.terminate_process()
                asyncio.wait(led_operation.rgb(
                    self.strip, self.bulb_1, self.bulb_2, led_request.r, led_request.g, led_request.b
                ))
            elif led_request.operation == "brightness":
                if self.led_process is not None:
                    current_operation = self.led_process.name
                    self.terminate_process()
                    led_operation.brightness(
                        self.strip, led_request.brightness)
                    self.led_process = Process(
                        target=getattr(led_operation, current_operation),
                        args=(self.strip,),
                    )
                    self.led_process.name = current_operation
                    self.led_process.start()
                else:
                    led_operation.brightness(
                        self.strip, led_request.brightness)
            elif led_request.operation == "rainbow":
                self.terminate_process()
                self.led_process = Process(
                    target=getattr(led_operation, led_request.operation),
                    args=(
                        self.strip,
                        led_request.wait_ms,
                    ),
                )
                self.led_process.name = led_request.operation
                self.led_process.start()
            else:
                self.terminate_process()
                self.led_process = Process(
                    target=getattr(led_operation, led_request.operation),
                    args=(self.strip,),
                )
                self.led_process.name = led_request.operation
                self.led_process.start()

        except AttributeError as e:
            print(
                f"{TerminalColors.WARNING}ERROR:\n {e.message}{TerminalColors.ENDC}")


if __name__ == "__main__":
    mqtt_client = MqttClient()
    asyncio.run(mqtt_client.bulb_init())
    print("Initialization completed successfully.")

    try:
        mqtt_client.client.loop_forever()
    except SystemError as e:
        mqtt_client.client.loop_stop()
