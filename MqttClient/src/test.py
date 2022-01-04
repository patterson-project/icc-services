import mqtt_client
import time

class Message:
    def __init__(self) -> None:
        self.payload = "color_wipe".encode("UTF-8")
        self.topic = "leds"

message = Message()
client = mqtt_client.MqttClient()
client.on_message("x", "x", message)

time.sleep(5)
message.payload = "off".encode("UTF-8")
client.on_message("x", "x", message)