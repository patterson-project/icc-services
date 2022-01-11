FROM debian:latest
RUN apt update -y && apt upgrade

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

RUN pip3 install rpi_ws281x paho-mqtt psutil

COPY src/*.py ./

EXPOSE 1883
CMD [ "python", "-u", "mqtt_client.py"]
