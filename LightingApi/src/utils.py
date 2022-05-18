import datetime
import paho.mqtt.client as MqttClient


def log(message):
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    print("[" + str(now.strftime("%Y-%m-%d %H:%M:%S")) + "]\t", end="")
    print(message)
