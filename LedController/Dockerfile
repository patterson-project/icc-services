FROM debian:latest
RUN apt update -y && apt upgrade -y

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

RUN pip3 install rpi_ws281x paho-mqtt python-kasa pygame

COPY src/*.py ./

EXPOSE 1883
CMD [ "python", "-u", "led_controller.py"]
