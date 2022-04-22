FROM debian:latest
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install python3-pygame -y

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /app

RUN pip3 install rpi_ws281x paho-mqtt python-kasa

COPY src/*.py ./

EXPOSE 1883
CMD [ "python", "-u", "led_controller.py"]
