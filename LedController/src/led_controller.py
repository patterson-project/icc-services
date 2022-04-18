import json
from multiprocessing.process import current_process
from kasa import SmartBulb
import paho.mqtt.client as mqtt
import led_operation
from rpi_ws281x import Adafruit_NeoPixel
from multiprocessing import Process
from utils import LedRequest, TerminalColors, LedConfig, log


class LedController:
    def __init__(self):
        self.strip = self.led_strip_init()
        self.client = self.mqtt_init()
        self.led_process = None
        self.operation_callback = {
            "rgb": self.rgb,
            "brightness": self.brightness,
            "rainbow": self.rainbow,
            "color_wipe": self.color_wipe,
            "sunrise": self.sunrise,
            "theater_chase": self.theater_chase,
            "rainbow_cycle": self.rainbow_cycle,
            "theater_chase_rainbow": self.theater_chase_rainbow,
        }

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
        client = mqtt.Client("led-controller", clean_session=False)
        client.connect(LedConfig.BROKER_ADDRESS)
        client.on_message = self.on_message
        client.subscribe("home/leds")
        return client

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
                led_operation.rgb(
                    self.strip,
                    led_request.r,
                    led_request.g,
                    led_request.b,
                )
            elif led_request.operation == "brightness":
                if self.led_process is not None:
                    current_operation = self.led_process.name
                    self.terminate_process()
                    led_operation.brightness(self.strip, led_request.brightness)
                    self.led_process = Process(
                        target=getattr(led_operation, current_operation),
                        args=(self.strip,),
                    )
                    self.led_process.name = current_operation
                    self.led_process.start()
                else:
                    led_operation.brightness(self.strip, led_request.brightness)
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
            print(f"{TerminalColors.WARNING}ERROR:\n {e.message}{TerminalColors.ENDC}")

    def rgb(self):
        pass

    def brightness(self):
        pass

    def rainbow(self):
        pass

    def color_wipe(self):
        pass

    def sunrise(self):
        pass

    def theater_chase(self):
        pass

    def rainbow_cycle(self):
        pass

    def theater_chase_rainbow(self):
        pass


if __name__ == "__main__":
    mqtt_client = LedController()
    print("Initialization completed successfully.")

    try:
        mqtt_client.client.loop_forever()
    except SystemError as e:
        mqtt_client.client.loop_stop()
