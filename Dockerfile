FROM debian:latest
RUN apt update -y && apt upgrade

FROM python:latest

LABEL Maintainer="canadrian72"

WORKDIR /usr/app

RUN pip3 install rpi_ws281x && \
    pip3 install paho-mqtt

COPY *.py ./

EXPOSE 1883
CMD [ "python", "./led_api.py"]