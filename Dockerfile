FROM debian:latest
RUN apt update -y && apt upgrade

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /usr/app

RUN pip3 install rpi_ws281x && \
    pip3 install paho-mqtt

COPY src/*.py ./

EXPOSE 1883
CMD [ "python", "-u", "led_api.py"]
